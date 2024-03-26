export const initCallme = () => {
    const popupTimer = $('#popup-timer');
    const url = '/api/call_me/';

    if (!popupTimer.length) {
        return
    }

    const form = popupTimer.find('.timer-popup-form');

    form.submit(function(e) {
        e.preventDefault();

        form.find('.timer-popup-submit').attr('disabled', 'disabled');

        let email = form.find('input[name="email"]').val();
        let telegram = form.find('input[name="telegram"]').val();
        let agree_processing = form.find('input[name="agree_processing"]').val();

        function success() {
            localStorage.setItem('popUpShownFlag', 'true');
            popupTimer.hide();
        }

        function error(data) {
            console.log(data)
        }

        const data = {
            "telegram": telegram,
            "email": email,
            "agree_processing": agree_processing,
        }


        $.ajax({
            type: "POST",
            url: url,
            data: data,
            success: success,
            error: error,
        })


    })



}


