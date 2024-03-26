export const initPopupShortlist = () => {
  const popupShortlist = $('.agro-shortlist-popup-shadow');

  if (!popupShortlist.length) {
      return
  }

  const closeBtn = $('.agro-shortlist-popup-close');
  let currentNomination = popupShortlist.attr('data-currnet-nomination');


  popupShortlist.on("mouseover", ".agro-shortlist-popup-header-nominations-item", function() {
    let element = $(this);
    let nominationTitle = element.attr('data-nomination-title');
    $('#short-list-popup-header-title').text(nominationTitle);
  });

  popupShortlist.on("mouseleave", ".agro-shortlist-popup-header-nominations", function() {
    currentNomination = popupShortlist.attr('data-currnet-nomination');
    $('#short-list-popup-header-title').text(currentNomination);
  });

  popupShortlist.on("click", ".agro-shortlist-popup-header-nominations-item", function() {
    let element = $(this);

    let nomination = element.attr('id').replace('short-list-popup-', '');
    let nominationTitle = element.attr('data-nomination-title');

    $('.agro-shortlist-popup-header-nominations-item').removeClass('agro-shortlist-popup-header-nominations-item_active');
    element.addClass('agro-shortlist-popup-header-nominations-item_active');

    $('#short-list-popup-header-title').text(nominationTitle);
    $('#short-list-popup-header-title').text(nominationTitle);
    popupShortlist.attr('data-currnet-nomination', nominationTitle);

    $('.agro-shortlist-popup-body').hide();
    $('#agro-shortlist-popup-container-' + nomination).show();

  });

  popupShortlist.on("click", ".agro-shortlist-popup-nominee-header", function() {
    let element = $(this);
    element.closest('.agro-shortlist-popup-nominee').toggleClass('agro-shortlist-popup-nominee_open');
  });


  closeBtn.click(function() {
      popupShortlist.hide();
      $('html').removeClass('fixed');
  });
}


