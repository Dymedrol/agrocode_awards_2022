import { initSelect } from './select';

export const initApplyForm = () => {

    const applyForm1 = $('#apply-form-1');

    if (!applyForm1.length) {
        return
    }

    const applyForm2 = $('#apply-form-2');
    const applyForm3 = $('#apply-form-3');
    const formStage = $('#form-stage');
    const prewBtn = $('#form-btn-prew');
    const nextBtn = $('#form-btn-next');

    const form1Url = '/api/first_step/';

    let currentStage = 1;
    let chosenNomination = '';

    applyForm1.submit(function(e) {
        e.preventDefault();

        let name = applyForm1.find('input[name="name"]').val();
        let surname = applyForm1.find('input[name="surname"]').val();
        let email = applyForm1.find('input[name="email"]').val();
        let phone = applyForm1.find('input[name="phone"]').val();
        let agree_processing = applyForm1.find('input[name="agree_processing"]').is(':checked');
        let agree_rules = applyForm1.find('input[name="agree_rules"]').is(':checked');

        let data = {
            "name": name,
            "surname": surname,
            "email": email,
            "phone": phone,
            "agree_processing": agree_processing,
            "agree_rules": agree_rules
        }

        function success() {
            applyForm1.hide();
            applyForm2.show();
            $("html, body").animate({ scrollTop: 0 }, "fast");
            currentStage = 2;
            formStage.text(currentStage);
            $('.agro-form-header-bottom-progress-bar').css('width', '66%');
            prewBtn.prop("disabled", false);
        }

        function error(data) {
            applyForm1.find('.agro-form-input-wrapper').removeClass('withError');
            let errors = data.responseJSON;
            // console.log(errors)

            for (let key of Object.keys(errors)) {
                let inputWithError = applyForm1.find('input[name="' + key + '"]');
                let wrapper = inputWithError.closest('.agro-form-input-wrapper');
                wrapper.addClass('withError');
                wrapper.find('.agro-form-input-error').text(errors[key]);
            }

            let clossestError = applyForm1.find('.withError').first();
            window.scrollTo(0, clossestError.offset().top - 100);
        }

        $.ajax({
            type: "POST",
            url: form1Url,
            data: data,
            success: success,
            error: error,
        })
    });

    applyForm2.submit(function(e) {
        e.preventDefault();
        chosenNomination = applyForm2.find('input:checked').val();
        let template = $('#' + chosenNomination + '-template').html();
        applyForm3.append(template);
        initSelect();

        applyForm2.hide();
        applyForm3.show();
        $("html, body").animate({ scrollTop: 0 }, "fast");
        currentStage = 3;
        formStage.text(currentStage);
        $('.agro-form-header-bottom-progress-bar').css('width', '100%');
        $('.agro-form-nav').addClass('agro-form-nav-3');
        nextBtn.text('Отправить заявку');
    });

    applyForm3.submit(function(e) {
        e.preventDefault();

        let name = applyForm1.find('input[name="name"]').val();
        let surname = applyForm1.find('input[name="surname"]').val();
        let email = applyForm1.find('input[name="email"]').val();
        let phone = applyForm1.find('input[name="phone"]').val();
        let agree_processing = applyForm1.find('input[name="agree_processing"]').is(':checked');
        let agree_rules = applyForm1.find('input[name="agree_rules"]').is(':checked');

        function sendNominationData(data, nomination) {
            let url = '/api/' + nomination + '/';

            function success() {
                localStorage.setItem('popUpShownFlag', 'true');
                $('#popup-success').show();
            }

            function error(data) {
                applyForm3.find('.wrapper-f3').removeClass('withError');
                let errors = data.responseJSON;
                console.log(errors);

                for (let key of Object.keys(errors)) {
                    let inputWithError = applyForm3.find('[name="' + key + '"]');
                    let wrapper = inputWithError.closest('.wrapper-f3');
                    wrapper.addClass('withError');
                    wrapper.find('.agro-form-input-error').text(errors[key]);
                }

                let clossestError = applyForm3.find('.withError').first();
                window.scrollTo(0, clossestError.offset().top - 50);

                $('#form-btn-next').addClass('agro-form-nav-btn_active').attr("disabled", false);
            }

            $('#form-btn-next').removeClass('agro-form-nav-btn_active').attr("disabled", true);

            $.ajax({
                type: "POST",
                url: url,
                data: data,
                success: success,
                error: error,
            })

        }

        let data = {
            "name": name,
            "surname": surname,
            "email": email,
            "phone": phone,
            "agree_processing": agree_processing,
            "agree_rules": agree_rules,
        }

        let data_upd = {};

        switch (chosenNomination) {
            case 'agro_machinery':
                let case_name = applyForm3.find('*[name="case_name"]').val();
                let company = applyForm3.find('*[name="company"]').val();
                let company_about = applyForm3.find('*[name="company_about"]').val();
                let company_url = applyForm3.find('*[name="company_url"]').val();
                let release_year = applyForm3.find('*[name="release_year"]').val();
                let initial_description = applyForm3.find('*[name="initial_description"]').val();
                let about_case = applyForm3.find('*[name="about_case"]').val();
                let about_result = applyForm3.find('*[name="about_result"]').val();
                let about_technology = applyForm3.find('*[name="about_technology"]').val();
                let about_uniq = applyForm3.find('*[name="company_about"]').val();
                let about_partners = applyForm3.find('*[name="about_partners"]').val();
                let extra_materials = applyForm3.find('*[name="extra_materials"]').val();

                data_upd = {
                    "case_name": case_name,
                    "company": company,
                    "company_about": company_about,
                    "company_url": company_url,
                    "release_year": release_year,
                    "initial_description": initial_description,
                    "about_case": about_case,
                    "about_result": about_result,
                    "about_technology": about_technology,
                    "about_uniq": about_uniq,
                    "about_partners": about_partners,
                    "extra_materials": extra_materials,
                }

                data = Object.assign(data, data_upd);
                break;
            case 'agro_digital':
                data_upd = {
                    "case_name": applyForm3.find('*[name="case_name"]').val(),
                    "company": applyForm3.find('*[name="company"]').val(),
                    "company_about": applyForm3.find('*[name="company_about"]').val(),
                    "company_url": applyForm3.find('*[name="company_url"]').val(),
                    "release_year": applyForm3.find('*[name="release_year"]').val(),
                    "initial_description": applyForm3.find('*[name="initial_description"]').val(),
                    "about_case": applyForm3.find('*[name="about_case"]').val(),
                    "about_result": applyForm3.find('*[name="about_result"]').val(),
                    "about_technology": applyForm3.find('*[name="about_technology"]').val(),
                    "about_uniq":  applyForm3.find('*[name="company_about"]').val(),
                    "about_partners": applyForm3.find('*[name="about_partners"]').val(),
                    "extra_materials": applyForm3.find('*[name="extra_materials"]').val(),
                }
                break;
            case 'future_food':
                data_upd = {
                    "case_name": applyForm3.find('*[name="case_name"]').val(),
                    "company": applyForm3.find('*[name="company"]').val(),
                    "company_about": applyForm3.find('*[name="company_about"]').val(),
                    "company_url": applyForm3.find('*[name="company_url"]').val(),
                    "release_year": applyForm3.find('*[name="release_year"]').val(),
                    "about_product": applyForm3.find('*[name="about_product"]').val(),
                    "about_process": applyForm3.find('*[name="about_process"]').val(),
                    "about_uniq": applyForm3.find('*[name="about_uniq"]').val(),
                    "production_volumes": applyForm3.find('*[name="production_volumes"]').val(),
                    "sales_market":  applyForm3.find('*[name="sales_market"]').val(),
                    "extra_materials": applyForm3.find('*[name="extra_materials"]').val(),
                }
                break;
            case 'made_in_russia':
                data_upd = {
                    "case_name": applyForm3.find('*[name="case_name"]').val(),
                    "company": applyForm3.find('*[name="company"]').val(),
                    "company_about": applyForm3.find('*[name="company_about"]').val(),
                    "company_url": applyForm3.find('*[name="company_url"]').val(),
                    "release_year": applyForm3.find('*[name="release_year"]').val(),
                    "release_month": applyForm3.find('*[name="release_month"]').val(),
                    "initial_description": applyForm3.find('*[name="initial_description"]').val(),
                    "about_technology": applyForm3.find('*[name="about_technology"]').val(),
                    "transition_process": applyForm3.find('*[name="transition_process"]').val(),
                    "about_result":  applyForm3.find('*[name="about_result"]').val(),
                    "about_partners": applyForm3.find('*[name="about_partners"]').val(),
                    "extra_materials": applyForm3.find('*[name="extra_materials"]').val(),
                }
                break;
            case 'agro_hero':

                let links = applyForm3.find('*[name="media_urls"]');
                let media_urls = '';

                links.each(function(index) {
                    media_urls = media_urls + $(this).val() + '\n';
                });

                data_upd = {
                    "nominate_fio": applyForm3.find('*[name="nominate_fio"]').val(),
                    "company": applyForm3.find('*[name="company"]').val(),
                    "company_about": applyForm3.find('*[name="company_about"]').val(),
                    "company_url": applyForm3.find('*[name="company_url"]').val(),
                    "role": applyForm3.find('*[name="role"]').val(),
                    "nomination_bio": applyForm3.find('*[name="nomination_bio"]').val(),
                    "achievements": applyForm3.find('*[name="achievements"]').val(),
                    "other_role": applyForm3.find('*[name="other_role"]').val(),
                    "media_urls": media_urls,
                }
                break;
            case 'agro_launch':
                data_upd = {
                    "project_name": applyForm3.find('*[name="project_name"]').val(),
                    "project_url": applyForm3.find('*[name="project_url"]').val(),
                    "company_about": applyForm3.find('*[name="company_about"]').val(),
                    "release_year": applyForm3.find('*[name="release_year"]').val(),
                    "release_month": applyForm3.find('*[name="release_month"]').val(),
                    "project_stage": applyForm3.find('*[name="project_stage"]').val(),
                    "project_sphere": applyForm3.find('*[name="project_sphere"]').val(),
                    "project_about": applyForm3.find('*[name="project_about"]').val(),
                    "about_technology": applyForm3.find('*[name="about_technology"]').val(),
                    "about_result":  applyForm3.find('*[name="about_result"]').val(),
                    "about_uniq": applyForm3.find('*[name="about_uniq"]').val(),
                    "founder": applyForm3.find('*[name="founder"]').val(),
                    "team": applyForm3.find('*[name="team"]').val(),
                    "extra_info": applyForm3.find('*[name="extra_info"]').val(),
                    "extra_materials": applyForm3.find('*[name="extra_materials"]').val(),
                }
                break;
            case 'agro_idea':
                let links2 = applyForm3.find('*[name="media_urls"]');
                let media_urls2 = '';

                links2.each(function(index) {
                    media_urls2 = media_urls2 + $(this).val() + '\n';
                });

                data_upd = {
                    "project_name": applyForm3.find('*[name="project_name"]').val(),
                    "project_date": applyForm3.find('*[name="project_date"]').val(),
                    "project_author": applyForm3.find('*[name="project_author"]').val(),
                    "project_about": applyForm3.find('*[name="project_about"]').val(),
                    "project_sphere": applyForm3.find('*[name="project_sphere"]').val(),
                    "about_uniq": applyForm3.find('*[name="about_uniq"]').val(),
                    "project_prototype": applyForm3.find('*[name="project_prototype"]').val(),
                    "about_technology": applyForm3.find('*[name="about_technology"]').val(),
                    "extra_info": applyForm3.find('*[name="extra_info"]').val(),
                    "extra_materials": applyForm3.find('*[name="extra_materials"]').val(),
                    "about_uniq": applyForm3.find('*[name="about_uniq"]').val(),
                    "media_urls": media_urls2,
                }
                break;
        }

        data = Object.assign(data, data_upd);

        sendNominationData(data, chosenNomination);

    });


    function nextBtnClickHandler() {
        switch (currentStage) {
            case 1:
                applyForm1.trigger('submit');
                break;
            case 2:
                applyForm2.trigger('submit');
                break;
            case 3:
                applyForm3.trigger('submit');
                break;
        }
    }

    function prewBtnClickHandler() {
        switch (currentStage) {
            case 1:
                break;
            case 2:
                applyForm2.hide();
                applyForm1.show();
                $("html, body").animate({ scrollTop: 0 }, "fast");
                currentStage = 1;
                formStage.text(currentStage);
                $('.agro-form-header-bottom-progress-bar').css('width', '33%');

                break;
            case 3:
                applyForm3.hide();
                applyForm3.empty()
                applyForm2.show();
                $("html, body").animate({ scrollTop: 0 }, "fast");
                currentStage = 2;
                formStage.text(currentStage);
                $('.agro-form-header-bottom-progress-bar').css('width', '66%');
                $('.agro-form-nav').removeClass('agro-form-nav-3');
                nextBtn.text('далее');
                break;
        }
    }

    prewBtn.click(prewBtnClickHandler);
    nextBtn.click(nextBtnClickHandler);

}


