let usluge=[
    {
        "usluga":"feniranje",
        "cena":1000,
        "kategorija":"frizer"
    },
    {
        "usluga":"gel lak",
        "cena":2000,
        "kategorija":"manikir"
    },
    {
        "usluga":"sisanje",
        "cena":700,
        "kategorija":"frizer"
    },
    {
        "usluga":"sminka",
        "cena":1000,
        "kategorija":"sminkanje"
    },
    {
        "usluga":"satiranje",
        "cena":3000,
        "kategorija":"frizer"
    },
    {
        "usluga":"izlivanje",
        "cena":2500,
        "kategorija":"manikir"
    }
];

let zaposleni= [
    {
        "id": 1, 
        "naslov": "Ana",
        "opis": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!",
        "specijalnost": "frizer",
        "starost": "9.75",
        "slika": "dodatno/Ana.jpeg",
        "link": "gospodjiceIzAvinjonaPonuda.html"
    },
    {
        "id": 2, 
        "naslov": "Mina",
        "opis": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!",
        "specijalnost": "frizer",
        "starost": "9.00 ",
        "slika": "dodatno/Mina.jpg",
        "link": "zenaKojaPlacePonuda.html"
    },
    {
        "id": 3, 
        "naslov": "Dunja",
        "opis": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!",
        "specijalnost": "sminkanje",
        "starost": "7.9",
        "slika": "dodatno/Dunja.jpg",
        "link": "gernikaPonuda.html"
    },
    {
        "id": 4, 
        "naslov": "Tijana",
        "opis": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!",
        "specijalnost": "sminkanje",
        "starost": "8.76",
        "slika": "dodatno/Tijana.jpg",
        "link": "damaSaHarmPonuda.html"
    },
    {
        "id": 5, 
        "naslov": "Tamara",
        "opis": " Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!",
        "specijalnost": "manikir",
        "starost": "9.5",
        "slika": "dodatno/Tamara.jpg",
        "link": "monaLizaPonuda.html"
    },
    {
        "id": 6, 
        "naslov": "Natasa",
        "opis": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!",
        "specijalnost": "manikir",
        "starost": "8.3",
        "slika": "dodatno/Natasa.jpg",
        "link": "tajnaVeceraPonuda.html"
    },

    {
        "id": 7, 
        "naslov": "Jana",
        "opis": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!",
        "specijalnost": "kozmeticar",
        "starost": "9.5",
        "slika": "dodatno/pera.jpeg",
        "link": "andjeoPonuda.html"
    },

    {
        "id": 8, 
        "naslov": "Nikolina",
        "opis": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia eveniet in cupiditate exercitationem ipsam, voluptate ab consequuntur tempore rem vel numquam tempora qui autem culpa iure, voluptates maxime nostrum, eligendi corrupti aut. Ab at alias neque, quaerat sint voluptas error laboriosam accusantium excepturi blanditiis quo laborum distinctio porro, natus omnis itaque dolore praesentium esse dolores quidem dicta fuga. Ipsam, id quas, eveniet deserunt perspiciatis natus sapiente nostrum earum facere necessitatibus ipsa labore tempora ut at, harum ad? Ipsum vero dignissimos deserunt necessitatibus magni quisquam exercitationem minus rem, at, facere, accusamus laboriosam temporibus dicta enim. Harum temporibus neque deleniti repudiandae maiores!.",
        "specijalnost": "kozmeticar",
        "starost": "8.9",
        "slika": "dodatno/nikolina.jpg",
        "link": "bahusPonuda.html"
    }

    
]

$(document).ready(function(){
    let html = '';
    for(let u of usluge){
        html += `<label class="container"><p>${u.usluga} &nbsp; ${u.cena}din</p>
        <input type="radio" checked="checked" name="radio" class="${u.kategorija}">
        <span class="checkmark"></span>
        </label>`;
    }
    
    $("#usluge").append(html);
    let customRadioStyles = `
    /* The container */
    .container {
        display: block;
        position: relative;
        padding-left: 35px;
        margin-bottom: 12px;
        cursor: pointer;
        font-size: 22px;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    label{
        font-size:15px !important;
    }
    /* Hide the browser's default radio button */
    .container input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
    }
    
    /* Create a custom radio button */
    .checkmark {
        position: absolute;
        top: 0;
        left: 0;
        height: 20px;
        width: 20px;
        background-color: #eee;
        border-radius: 50%;
    }
    
    /* On mouse-over, add a grey background color */
    .container:hover input ~ .checkmark {
        background-color: #ccc;
    }
    
    /* When the radio button is checked, add a blue background */
    .container input:checked ~ .checkmark {
        background-color: #2196F3;
    }
    
    /* Create the indicator (the dot/circle - hidden when not checked) */
    .checkmark:after {
        content: "";
        position: absolute;
        display: none;
    }
    
    /* Show the indicator (dot/circle) when checked */
    .container input:checked ~ .checkmark:after {
        display: block;
    }
    
    /* Style the indicator (dot/circle) */
    .container .checkmark:after {
        top: 9px;
        left: 9px;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: white;
    }`;

    let styleElement = document.createElement("style");
    styleElement.innerHTML = customRadioStyles;
    document.head.appendChild(styleElement);

    popuniZaposlene();
    $('input[type="radio"]').change(function() {
        popuniZaposlene();

})

});

function popuniZaposlene(){
    let checkedRadioButton = $('input[type="radio"]:checked');
        // Ako postoji čekirani radio button
        if (checkedRadioButton.length > 0) {
            // Dohvati klasu čekiranog radio button-a
            let radioClass = checkedRadioButton.attr('class');
            
            // Proveri da li radio dugme ima postavljenu klasu
            if (radioClass) {
                let classArray = radioClass.split(' ');
                let lastClass = classArray[classArray.length - 1];
                
                html='<h6>Odaberite zaposlenog:</h6>';
                $("#zaposleni").html(html);
                html='';
                for(let z of zaposleni){
                    if(lastClass==z.specijalnost)
                    {   
                        html += `<label class="container"><p>${z.naslov} &nbsp; (${z.starost})</p>
                        <input type="radio" checked="checked" name="radio1">
                        <span class="checkmark"></span>
                        </label>`;
                    
                    }
                }
                $("#zaposleni").append(html);


            } else {
                console.log("Radio dugme nema postavljenu klasu.");
            }
        } else {
            console.log("Nijedan radio button nije čekiran.");
        }
}