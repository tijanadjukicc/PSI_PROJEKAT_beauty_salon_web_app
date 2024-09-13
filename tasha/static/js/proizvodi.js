$(document).ready( function() {
        $('.love').click(function() {
            let loveColor = $(this).css('color');
            if( loveColor == 'rgb(0, 0, 0)') {
                $(this).css('color', 'red');
            }
            else {
                $(this).css('color', 'rgb( 0, 0, 0)');
            }
        })
    }
);

$(document).ready(function (){
    $('.proizvod').hide();
    $('#vise1').click(function (){
        $('#prvi').show();
    })
    $('#vise2').click(function (){
        $('#drugi').show();
    })
    $('#vise3').click(function (){
        $('#treci').show();
    })
    
    $('.iks-novi').click(function (){
        $('.proizvod').hide();
    })
   
});