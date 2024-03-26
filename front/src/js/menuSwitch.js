export const initMenuSwitch = () => {

    let windowWith = $( window ).width();
    let scrollSpace = 100;
    let headerHight = $('.agro-header').outerHeight() + 20;
    let idicator = $("#indicator");
    let indicatorItems = idicator.find('.agro-indicator-item');

    if (windowWith >= 1300) {
        scrollSpace = 200;
    }

    $(window).resize(function() {
        headerHight = $('.agro-header').outerHeight() + 20;
        windowWith = $( window ).width();
    });

    $(document).on('click', 'a[href^="#"]', function (event) {
        event.preventDefault();

        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top - headerHight
        }, 500);
    });

    let lastId;
    let menu = $('.agro-aside');
    let menuItems = menu.find('a[href^="/#"]');
    let mobileMenu = $('.agro-mobile-menu-inner');
    let mobileMenuItems = mobileMenu.find('a[href^="/#"]');

    let scrollItems = menuItems.map(function(){
        var link = $(this).attr("href").replace('/', '')
        var item = $(link);
        if (item.length) {
            return item;
        }
    });



    $(window).scroll(function(){
        let fromTop = $(this).scrollTop();
        let curIndex = 0;

        let cur = scrollItems.map(function(index){
            if ($(this).offset().top < fromTop + scrollSpace) {
                curIndex = index;
                return this;
            }
        });

        indicatorItems.removeClass('agro-indicator-item_active');
        indicatorItems.eq(curIndex).addClass('agro-indicator-item_active');

        cur = cur[cur.length - 1];
        var id = cur && cur.length ? cur[0].id : "";

        if (lastId !== id) {
            lastId = id;
            menuItems.removeClass("agro-aside-item_active");
            menuItems.filter("[href='/#"+id+"']").addClass("agro-aside-item_active");

            mobileMenuItems.removeClass("agro-mobile-menu-item_active");
            mobileMenuItems.filter("[href='/#"+id+"']").addClass("agro-mobile-menu-item_active");
        }
    });

}


