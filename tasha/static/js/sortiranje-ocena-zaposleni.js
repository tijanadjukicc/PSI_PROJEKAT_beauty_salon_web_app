$(document).ready(function (){
    $('.button-filter-wrapper button').click(function (){
        if (!$('#ocena-opadajuca').is(':checked') && !$('#ocena-rastuca').is(':checked')) return;

        event.preventDefault();
        $('#filter-menu').hide();
        $('.card-col').hide();
        
        let articleIds = $('.card-col').map(function() {
            return this.id;
        }).get();
    
        articleIds.sort((a, b) => {
            let ocenaA = parseFloat($('#'+a+' .ocena').text().match(/(\d+(\.\d+)?)/)?.[1]);
            let ocenaB = parseFloat($('#'+b+' .ocena').text().match(/(\d+(\.\d+)?)/)?.[1]);
    
            ocenaA = isNaN(ocenaA) ? 0 : ocenaA;
            ocenaB = isNaN(ocenaB) ? 0 : ocenaB;
    
            return ocenaA - ocenaB;
        });

        console.log(articleIds)
        if ($('#ocena-opadajuca').is(':checked')) {
            articleIds.reverse();
        } 
        
        articleIds.forEach(article => {
            $('#'+article).show(); // Show the article
            $('.content').append($('#'+article)); // Move the article to the end
        });
    });

});
