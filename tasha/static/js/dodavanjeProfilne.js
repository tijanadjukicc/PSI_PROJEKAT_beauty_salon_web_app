$(document).ready(function (){
    $('#input-image').on('change', function(event) {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = function(e) {
            const imageUrl = e.target.result;
            $('#slika-novog').hide();
            $('#slika-novog').attr('src', imageUrl).show();
          };
          reader.readAsDataURL(file);
        }
    });
})