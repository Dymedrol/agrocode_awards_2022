export const initPopupTimer = () => {

    const popupTimer = $('#popup-timer');
    const applyButton = $('.agro-header-controls-submit');

    if (!popupTimer.length) {
        return
    }

    if (applyButton.hasClass('hidden')) {
        return
    }

    let popUpShownFlag = localStorage.getItem('popUpShownFlag');

    if (popUpShownFlag) {
        return
    }

    $('.timer-popup__close').click(function() {
        localStorage.setItem('popUpShownFlag', 'true');
        popupTimer.hide();
    });

    function openPopup() {
      popupTimer.show();
    }

    setTimeout(openPopup, 20000);

}


