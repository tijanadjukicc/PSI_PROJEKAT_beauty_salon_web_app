$(document).ready(function (){
    $('.novi-proizvod').hide();
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
        $('.novi-proizvod').hide();
    })
   
});