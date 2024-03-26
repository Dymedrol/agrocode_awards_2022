export const initHeaderSticker = () => {
    const burgerWrapper = $('#burger-wrapper');
    const header = $('#agro-header');


    function checkOffset() {
        if ($(document).scrollTop() > 0) {
            header.addClass('agro-header_with-back');
            burgerWrapper.addClass('agro-header-burger_with-back');
        } else {
            header.removeClass('agro-header_with-back');
            burgerWrapper.removeClass('agro-header-burger_with-back');
        }
    }

    checkOffset();

    $(document).scroll(function() {
        checkOffset();
    });

}


