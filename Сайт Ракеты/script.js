document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector('header');
    const container = document.querySelector('#container');
    const menuButton = document.querySelector('#menu');
    const linksContainer = document;

    function handleScroll() {
        container.classList.toggle('menuopen', false);
        header.classList.toggle('sticky', window.scrollY >= 10);
    }

    function handleMenuButtonClick() {
        container.classList.toggle('menuopen');
        header.classList.remove('sticky');
    }

    function handleLinkClick(event) {
        event.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    }

    function handleCloseOutside(event) {
        if (!menuButton.contains(event.target)) {
            container.classList.remove('menuopen');
            header.classList.add('sticky');
        }
    }

    document.addEventListener('scroll', (event) => {
        handleScroll();
        handleCloseOutside(event);
    });

    menuButton.addEventListener('click', handleMenuButtonClick);

    linksContainer.addEventListener('click', (event) => {
        if (event.target.tagName === 'A' && event.target.getAttribute('href').startsWith('#')) {
            handleLinkClick.call(event.target, event);
        } else {
            handleCloseOutside(event);
        }
    });
});
