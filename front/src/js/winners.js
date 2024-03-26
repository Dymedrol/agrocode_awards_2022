export const initWinners = () => {
  const winnersBlock = $('.agro-winners');

  if (!winnersBlock.length) {
    return;
  }

  const sliderWrapper = winnersBlock.find('.agro-winners-slider-wrapper');
  const nominationsNav = winnersBlock.find('.agro-winners-nominations');
  const owlwinnersBlock = $('.agro-winners-slider-inner');

  const prewBtn = '<div class="agro-winners-slider-nav-prev js-agro-short-list-prev"><svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg"><circle r="39" transform="matrix(-1 0 0 1 40 40)" fill="#020312" stroke="white" stroke-width="2"/><path d="M43.5486 53.3345L32.24 42.0259C31.0684 40.8543 31.0684 38.9548 32.24 37.7832L43.5486 26.4746" stroke="#4CED5B" stroke-width="2"/></svg></div>';
  const nextBtn = '<div class="agro-winners-slider-nav-next js-agro-short-list-next"><svg width="80" height="80" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="40" cy="40" r="39" fill="#020312" stroke="white" stroke-width="2"/><path d="M36.4514 53.3345L47.76 42.0259C48.9316 40.8543 48.9316 38.9548 47.76 37.7832L36.4514 26.4746" stroke="#4CED5B" stroke-width="2"/></svg></div>';


  function checkArrows(event) {
    var element = $(event.target);
    var activeElement = element.find('.center');
    var activeNomination = activeElement.find('.agro-winners-slider-item').attr('data-nomination');
    nominationsNav.find('.agro-winners-nominations-item').removeClass('agro-winners-nominations-item_active');
    nominationsNav.find('#winners-' + activeNomination).addClass('agro-winners-nominations-item_active');

    var items = event.item.count;
    var item  = event.item.index + 1;
    var prev = element.find('.agro-winners-slider-nav-prev');
    var next = element.find('.agro-winners-slider-nav-next');

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

  owlwinnersBlock.owlCarousel({
      loop:false,
      center: true,
      autoWidth: true,
      mouseDrag: true,
      onTranslated: checkArrows,
      onInitialized: checkArrows,
      navText: [prewBtn, nextBtn],
      smartSpeed: 700,
      responsive:{
          0:{
              items:1,
              nav: false,
              center: true,
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
    var matrix = winnersBlock.find('.owl-stage').css('transform').replace(/[^0-9\-.,]/g, '').split(',');
    var x = matrix[12] || matrix[4];
    var paddingLeft = winnersBlock.find('.agro-winners-header').css('padding-left');
    paddingLeft = parseInt(paddingLeft, 10);
    sliderWrapper.css('margin-left', -x + paddingLeft);
  }



  nominationsNav.on("click", ".agro-winners-nominations-item", function() {
    let element = $(this);
    let elementIndex = element.index();
    owlwinnersBlock.trigger('to.owl.carousel', elementIndex)
  });

  $('.js-agro-winners-prev').click(function() {
      owlwinnersBlock.trigger('prev.owl.carousel');
  })

  $('.js-agro-winners-next').click(function() {
      owlwinnersBlock.trigger('next.owl.carousel');
  })

  $('.agro-winners-slider-item-btn').click(function() {
    let element = $(this);
    let nomination = element.closest('.agro-winners-slider-item').attr('data-nomination');
    $('.agro-shortlist-popup-shadow').show();
    $('.agro-shortlist-popup-header-nominations-item').removeClass('agro-shortlist-popup-header-nominations-item_active');
    $('#short-list-popup-' + nomination).addClass('agro-shortlist-popup-header-nominations-item_active');
    $('html').addClass('fixed');
    $('.agro-shortlist-popup-body').hide();
    let nominationTitle = element.closest('.agro-winners-slider-item').find('.agro-winners-slider-item-nomination').text();
    nominationTitle = nominationTitle.replace('Номинация:', '');
    $('.agro-shortlist-popup-shadow').attr('data-currnet-nomination', nominationTitle);
    $('#short-list-popup-header-title').text(nominationTitle);
    $('#agro-shortlist-popup-container-' + nomination).show();
  });


}


