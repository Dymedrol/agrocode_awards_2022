export const initShortList = () => {
  const shortList = $('.agro-short-list');

  if (!shortList.length) {
    return;
  }

  const sliderWrapper = shortList.find('.agro-short-list-slider-wrapper');
  const nominationsNav = shortList.find('.agro-short-list-nominations');
  const owlShortList = $('.agro-short-list-slider-inner');

  const prewBtnTablet = $('.js-agro-short-list-prev');
  const nextBtnTablet = $('.js-agro-short-list-next');

  const prewBtn = '<div class="agro-short-list-slider-nav-prev js-agro-short-list-prev"><svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg"><circle r="39" transform="matrix(-1 0 0 1 40 40)" fill="#020312" stroke="white" stroke-width="2"/><path d="M43.5486 53.3345L32.24 42.0259C31.0684 40.8543 31.0684 38.9548 32.24 37.7832L43.5486 26.4746" stroke="#4CED5B" stroke-width="2"/></svg></div>';
  const nextBtn = '<div class="agro-short-list-slider-nav-next js-agro-short-list-next"><svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="40" cy="40" r="39" fill="#020312" stroke="white" stroke-width="2"/><path d="M36.4514 53.3345L47.76 42.0259C48.9316 40.8543 48.9316 38.9548 47.76 37.7832L36.4514 26.4746" stroke="#4CED5B" stroke-width="2"/></svg></div>';

  nominationsNav.click(function(e) {
    let target = $(e.target);
    let chosenNomination = '';
    let btn;

    if (target.hasClass('agro-short-list-nominations-item')) {
      chosenNomination = target.attr('id');
      btn = target;
    }

    if (target.closest('.agro-short-list-nominations-item').length) {
      chosenNomination = target.closest('.agro-short-list-nominations-item').attr('id');
      btn = target.closest('.agro-short-list-nominations-item');
    }

    if (chosenNomination) {
      nominationsNav.find('.agro-short-list-nominations-item').removeClass('agro-short-list-nominations-item_active');
      btn.addClass('agro-short-list-nominations-item_active');
      sliderWrapper.find('.agro-short-list-slider-inner').removeClass('open');
      sliderWrapper.find('#' + chosenNomination + '-slider').addClass('open');
    }
  });

  function checkArrows(event) {
    var element = $(event.target);
    var items = event.item.count;
    var item  = event.item.index + 1;
    var prev = element.find('.agro-short-list-slider-nav-prev');
    var next = element.find('.agro-short-list-slider-nav-next');

      if (item == 1 && items == 1) {
          next.hide();
          prev.hide();
      }
      else if  (item >= items){
          next.hide();
          prev.show();
      }
      //disable previus
      else if (item == 1) {
          next.show();
          prev.hide();
      }
      else {
          prev.show();
          next.show();
      }
  };

  owlShortList.owlCarousel({
      loop:false,
      center: true,
      autoWidth: true,
      mouseDrag: true,
      nav: true,
      onTranslated: checkArrows,
      onInitialized: checkArrows,
      navText: [prewBtn, nextBtn],
      smartSpeed: 700,
      responsive:{
          0:{
              items:2,
              nav: false,
          },
          768:{
              items: 1,
              nav: false,
          },
          1024:{
              items: 1,
              nav: true,
          },
          1366:{
              items: 1,
              nav: true,
          },
          1920:{
              items: 1,
              nav: true,
          }
      }
  })

  if ($(window).width() < 719) {
    var matrix = shortList.find('.owl-stage').css('transform').replace(/[^0-9\-.,]/g, '').split(',');
    var x = matrix[12] || matrix[4];
    var paddingLeft = shortList.find('.agro-short-list-header').css('padding-left');
    paddingLeft = parseInt(paddingLeft, 10);
    sliderWrapper.find('.owl-stage-outer').css('margin-left', -x + paddingLeft);
  }

  prewBtnTablet.click(function() {
      owlShortList.trigger('prev.owl.carousel');
  })

  nextBtnTablet.click(function() {
      owlShortList.trigger('next.owl.carousel');
  })
}


