$(document).ready(function (){
    $('#filter-menu').hide();
    $('.filter i').click(function (){
        $('#filter-menu').toggle();
    })

    $('#search-button-wrapper').hide();
    $('#formaPretraga').on('focusin mouseenter', function() {
        $('#search-button-wrapper').show();
    });

    $('.search-wrapper').on('focusout mouseleave', function() {
        $('#search-button-wrapper').hide();
    });
})

