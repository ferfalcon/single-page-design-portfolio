import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';

const root = '/vercel/path0';
const frontend = '/vercel/path1';
const cli = 'docs/implementation-workflow/cli/design-workflow.mjs';
const output = join(frontend, 'public', 'workflow-output');

function run(args, { capture = false } = {}) {
  const result = execFileSync('node', [cli, ...args], {
    cwd: root,
    encoding: 'utf8',
    stdio: capture ? ['ignore', 'pipe', 'inherit'] : 'inherit',
  });
  return capture ? result : '';
}

function readJsonCommand(args) {
  return JSON.parse(run(args, { capture: true }));
}

console.log('=== Repair deterministic generated projections ===');
run(['sync']);
run(['sync', '--check']);

console.log('=== Canonical context before retry ===');
const contextBefore = readJsonCommand(['context', '--json']);
console.log(JSON.stringify(contextBefore, null, 2));

if (contextBefore.stage?.number !== 0) {
  throw new Error(`Expected canonical Stage 0 before retry; got Stage ${contextBefore.stage?.number}.`);
}

const auditPath = join(root, 'DESIGN-AUDIT.md');
const auditBackup = '/tmp/DESIGN-AUDIT.md';
if (!existsSync(auditPath)) throw new Error('DESIGN-AUDIT.md is missing from the PR branch checkout.');
cpSync(auditPath, auditBackup);
rmSync(auditPath);

console.log('=== Advance Stage 0 -> Stage 1 with the canonical CLI ===');
run(['stage', 'advance']);

cpSync(auditBackup, auditPath);

console.log('=== Review and approve ART-DESIGN-AUDIT ===');
run([
  'artifact', 'review', 'ART-DESIGN-AUDIT',
  '--evidence', 'Stage 1 design audit completed against SRC-DS-001; two audit review passes completed and owner resolutions recorded.',
]);
run([
  'artifact', 'approve', 'ART-DESIGN-AUDIT',
  '--evidence', 'Project owner approved the Stage 1 design audit and its recorded owner resolutions.',
  '--approved-by', 'Fernando Falcon',
]);

console.log('=== Stage 1 preflight ===');
const checkBefore = readJsonCommand(['stage', 'check', '--json']);
console.log(JSON.stringify(checkBefore, null, 2));
if (checkBefore.decision?.recommendedResult !== 'Passed' || !checkBefore.decision?.recordable) {
  throw new Error(`Stage 1 preflight did not recommend Passed: ${JSON.stringify(checkBefore.decision)}`);
}

console.log('=== Record Stage 1 owner approval; do NOT advance Stage 2 ===');
run([
  'stage', 'review',
  '--result', 'Passed',
  '--evidence', 'Stage 1 design audit passed CLI preflight; the project owner approved Stage 1 and explicitly deferred Stage 2 advancement.',
  '--approved-by', 'Fernando Falcon',
]);

console.log('=== Validate parked Stage 1 state ===');
const checkAfter = readJsonCommand(['stage', 'check', '--json']);
const contextAfter = readJsonCommand(['context', '--json']);
console.log(JSON.stringify(checkAfter, null, 2));
console.log(JSON.stringify(contextAfter, null, 2));
run(['sync', '--check']);
run(['validate']);

const recordPath = join(root, '.workflow', 'workflow-record.json');
const record = JSON.parse(readFileSync(recordPath, 'utf8'));
const stage1Gate = [...record.gates].reverse().find((gate) => gate.stage === 1 && gate.status === 'Active');
if (record.state.stage !== 1 || record.state.status !== 'Ready') {
  throw new Error(`Expected Stage 1 Ready, received ${JSON.stringify(record.state)}.`);
}
if (!stage1Gate || !['Passed', 'Passed with assumptions'].includes(stage1Gate.result)) {
  throw new Error('Expected an active passing Stage 1 gate.');
}

mkdirSync(join(output, 'generated'), { recursive: true });
cpSync(recordPath, join(output, 'workflow-record.json'));
for (const name of ['WORKFLOW-STATUS.md', 'SOURCE-INDEX.md', 'ARTIFACT-INDEX.md', 'TASK-INDEX.md', 'TRACEABILITY.md']) {
  cpSync(join(root, '.workflow', 'generated', name), join(output, 'generated', name));
}
cpSync(auditPath, join(output, 'DESIGN-AUDIT.md'));
writeFileSync(join(output, 'stage1-check-before.json'), `${JSON.stringify(checkBefore, null, 2)}\n`);
writeFileSync(join(output, 'stage1-check-after.json'), `${JSON.stringify(checkAfter, null, 2)}\n`);
writeFileSync(join(output, 'context-after.json'), `${JSON.stringify(contextAfter, null, 2)}\n`);
console.log('STAGE1_GATE_OUTPUT_READY');
