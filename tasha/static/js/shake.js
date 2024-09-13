function shake() {
    let randId0 = Math.floor(Math.random()*6);
    let randId1;

    while ((randId1 = Math.floor(Math.random()*6)) ==  randId0);

    $('img').removeClass('shaker');
    
    $('#dryer'+randId0).addClass('shaker');
    $('#dryer'+randId1).addClass('shaker');
}

function callShaker() {
    handler = setInterval(shake, 4000);
}

$(document).ready(function () {
    callShaker();
})