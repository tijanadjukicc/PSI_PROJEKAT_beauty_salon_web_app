from django.contrib import admin
from . models import  *

# Register your models here.
admin.site.register(Admin)

admin.site.register(Budzetsalona)
admin.site.register(Kategorija)
admin.site.register(Korisnik)
admin.site.register(KorisnikHasProizvod)
admin.site.register(Musterija)
admin.site.register(Narucenproizvod)

admin.site.register(Narudzbina)

admin.site.register(Ocena)

admin.site.register(Popusti)

admin.site.register(Proizvod)

admin.site.register(Radnidan)

admin.site.register(Raspored)

admin.site.register(Rezervacija)

admin.site.register(Slobodantermin)

admin.site.register(Tretman)

admin.site.register(Zaposleni)