$(document).ready(function () {
    // Selektuj sva dugmad sa klasom 'zakazi'
    var buttons = $(".zakazi");
    
    // Dodaj 'click' događaj za svako dugme
    buttons.on("click", function() {
        window.location.href = "nalog.html";
    });
});