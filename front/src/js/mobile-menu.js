export const initMobileMenu = () => {
    const burger = $('#burger');
    const mobileMenu = $('#mobile-menu');
    const closeBtn = $('#mobile-menu-close');
    const mobileMenuItems = mobileMenu.find('.agro-mobile-menu-item');

    burger.click(function() {
        mobileMenu.show();
    });

    closeBtn.click(function() {
        mobileMenu.hide();
    });

    mobileMenuItems.click(function() {
        mobileMenu.hide();
    });
}


