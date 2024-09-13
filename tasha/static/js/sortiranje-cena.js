let vrste_rpoizvoda = [
    'krema',
    'sampon',
    'maska-za-kosu'
]

$(document).ready(function (){
    $('.button-filter-wrapper button').click(function (){
        if (!$('#cena-opadajuca').is(':checked') && !$('#cena-rastuca').is(':checked')) return;

        // event.preventDefault();
        $('#filter-menu').hide();
        $('article').hide();
        
        let articleIds = $('article').map(function() {
            return this.id;
        }).get();
    
        articleIds.sort((a, b) => {
            let cenaA = parseFloat($('#'+a).text().match(/(\d+(\.\d+)?)din/)?.[1]);
            let cenaB = parseFloat($('#'+b).text().match(/(\d+(\.\d+)?)din/)?.[1]);
    
            cenaA = isNaN(cenaA) ? 0 : cenaA;
            cenaB = isNaN(cenaB) ? 0 : cenaB;
    
            return cenaA - cenaB;
        });

        if ($('#cena-opadajuca').is(':checked')) {
            articleIds.reverse();
        } 
        
        articleIds.forEach(article => {
            $('#'+article).show(); // Show the article
            $('.articles').append($('#'+article)); // Move the article to the end
        });
    });

});
