$(document).ready(function (){
    $('.novi-proizvod').hide();
    $('#dodaj-novi-dugme').click(function (){
        $('.novi-proizvod').show();
    })
    
    $('.iks-novi').click(function (){
        $('.novi-proizvod').hide();
    })
    // $('#search-button-wrapper').hide();
    // $('.search').click(function (){
    //     $('#search-button-wrapper').toggle();
    // })

    // $('.button-filter-wrapper button').click(function (){
    //     event.preventDefault();
    //     $('#filter-menu').hide();
    //     $('article').hide()
        
    //     vrste_rpoizvoda.forEach(function (proizvod) {
    //         if($('#'+proizvod).prop('checked')) {
    //             $('.'+proizvod).show();
    //         }
    //     })
    // })
})