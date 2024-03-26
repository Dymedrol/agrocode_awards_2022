export const initFaqAccordion = () => {
    const faqItemsTop = $('.agro-faq-item-top');

    faqItemsTop.click(function() {
        $(this).closest('.agro-faq-item').toggleClass('agro-faq-item_open');
    });
}


