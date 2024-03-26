
import '../less/index.less';

import { initMobileMenu } from './mobile-menu';
import { initHeaderSticker } from './headerSticker';
import { initMenuSwitch } from './menuSwitch';
import { initFaqAccordion } from './faqAccordion';
import { initSelect } from './select';
import { initPopupTimer } from './popupTimer'
import { initCallme } from './callMe';
import { initAnimation } from './animation';
import { initApplyForm } from './apply-form';
import { initShortList } from './short-list';
import { initWinners } from './winners';
import { initPopupShortlist } from './popup-short-list';


document.addEventListener("DOMContentLoaded", function() {
    initMobileMenu();
    initHeaderSticker();
    initMenuSwitch();
    initFaqAccordion();
    initSelect();
    initCallme();
    initPopupTimer();
    initApplyForm();
    initAnimation();
    initShortList();
    initWinners();
    initPopupShortlist();

    $('body').addClass('body-background');

    const owl = $('.agro-jury-wrapper');

    owl.owlCarousel({
        loop:true,
        margin: 10,
        center: true,
        autoWidth: true,
        responsive:{
            0:{
                items:2,
            },
            768:{
                items: 4,
            },
            1024:{
                items: 5,
                loop:true,
            },
            1920:{
                items: 6,
                loop:true,
            }
        }
    })

    $('#prev-btn').click(function() {
        owl.trigger('prev.owl.carousel');
    })

    $('#next-btn').click(function() {
        owl.trigger('next.owl.carousel');
    })

    var lazyLoadInstance = new LazyLoad({
    // Your custom settings go here
    })

    jQuery(document).ajaxSend(function(event, xhr, settings) {
        function getCookie(name) {
            // Хуку для ajax свой метод.
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        function sameOrigin(url) {
            // url could be relative or scheme relative or absolute
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        }
        function safeMethod(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });

    function setCookie(name, value, options) {
        options = options || {};

        var expires = options.expires;

        if (typeof expires == "number" && expires) {
            var d = new Date();
            d.setTime(d.getTime() + expires * 1000);
            expires = options.expires = d;
        }
        if (expires && expires.toUTCString) {
            options.expires = expires.toUTCString();
        }

        value = encodeURIComponent(value);

        var updatedCookie = name + "=" + value;

        for (var propName in options) {
            updatedCookie += "; " + propName;
            var propValue = options[propName];
            if (propValue !== true) {
                updatedCookie += "=" + propValue;
            }
        }

        document.cookie = updatedCookie;
    }

    function deleteCookie(name) {
      setCookie(name, "", {
        expires: -1
      })
    }


})
