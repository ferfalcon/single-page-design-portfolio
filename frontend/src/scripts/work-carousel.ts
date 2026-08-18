const carousels = document.querySelectorAll<HTMLElement>('[data-work-carousel]');

carousels.forEach((root) => {
  const carousel = root.querySelector<HTMLElement>('.work-carousel');
  const slides = Array.from(root.querySelectorAll<HTMLElement>('[data-carousel-slide]'));
  const controls = root.querySelector<HTMLElement>('[data-carousel-controls]');
  const previousButton = root.querySelector<HTMLButtonElement>('[data-carousel-previous]');
  const nextButton = root.querySelector<HTMLButtonElement>('[data-carousel-next]');
  const status = root.querySelector<HTMLElement>('[data-carousel-status]');

  if (!carousel || slides.length === 0 || !controls || !previousButton || !nextButton || !status) {
    return;
  }

  const reducedMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  const tabletQuery = window.matchMedia('(min-width: 48rem)');
  let activeIndex = Math.min(2, slides.length - 1);
  let isAnimating = false;
  const inputQueue: number[] = [];

  const shortestOffset = (index: number) => {
    let offset = index - activeIndex;
    const halfway = Math.floor(slides.length / 2);

    if (offset > halfway) offset -= slides.length;
    if (offset < -halfway) offset += slides.length;

    return offset;
  };

  const render = (animate: boolean) => {
    const slideWidth = slides[0]?.getBoundingClientRect().width ?? 0;
    const gap = tabletQuery.matches ? 32 : 20;

    slides.forEach((slide, index) => {
      const nextOffset = shortestOffset(index);
      const previousOffset = Number(slide.dataset.offset);
      const shouldAnimate =
        animate &&
        !reducedMotionQuery.matches &&
        Number.isFinite(previousOffset) &&
        Math.abs(previousOffset - nextOffset) === 1;

      slide.dataset.animate = shouldAnimate ? 'true' : 'false';
      slide.dataset.offset = String(nextOffset);
      slide.style.setProperty('--carousel-x', `${nextOffset * (slideWidth + gap)}px`);

      if (index === activeIndex) {
        slide.setAttribute('aria-current', 'true');
      } else {
        slide.removeAttribute('aria-current');
      }
    });
  };

  const announce = () => {
    status.textContent = `Project ${activeIndex + 1} of ${slides.length}`;
  };

  const processQueue = () => {
    if (isAnimating || inputQueue.length === 0) return;

    const direction = inputQueue.shift();
    if (direction === undefined) return;

    isAnimating = true;
    activeIndex = (activeIndex + direction + slides.length) % slides.length;
    render(true);

    window.setTimeout(
      () => {
        announce();
        isAnimating = false;
        processQueue();
      },
      reducedMotionQuery.matches ? 0 : 210,
    );
  };

  const enqueue = (direction: number) => {
    inputQueue.push(direction);
    processQueue();
  };

  previousButton.addEventListener('click', () => enqueue(-1));
  nextButton.addEventListener('click', () => enqueue(1));

  carousel.classList.add('is-enhanced');
  render(false);
  controls.hidden = false;
  root.dataset.carouselReady = 'true';

  const handleLayoutChange = () => render(false);
  tabletQuery.addEventListener('change', handleLayoutChange);
  reducedMotionQuery.addEventListener('change', handleLayoutChange);

  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(handleLayoutChange);
    observer.observe(root);
  } else {
    window.addEventListener('resize', handleLayoutChange, { passive: true });
  }
});
