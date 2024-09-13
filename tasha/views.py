from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseServerError
from .models import *
from django.shortcuts import render, redirect
from .forms import *
from datetime import date, datetime
from django.db.models import Avg, Max
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import os

# prikaz proizvoda - TIJANA DJUKIC
# soritanje proizvoda - TIJANA DJUKIC
# pretraga proizvoda - TIJANA DJUKIC
def prikazProizvoda(request):
    jedanProizvod = ''
    proizvodi = Proizvod.objects.all()
    kategorije = [(kat.naziv, kat.naziv) for kat in Kategorija.objects.all()]

    if request.method == 'POST':
        formKat = FilterProductsKategorijaForm(request.POST, categories=kategorije)
        formSearch = SearchForm(request.POST)

        if formKat.is_valid(): #izvlacenje proizvoda po odabranim kategorijama
            odabraneKategorije = formKat.cleaned_data.get('kategorije')
            if odabraneKategorije:
                odabraneKategorijeId = Kategorija.objects.filter(naziv__in=odabraneKategorije).values_list('idkat', flat=True)
                proizvodi = Proizvod.objects.filter(kategorija_idkat__in=odabraneKategorijeId)

            odabranaOpcija = formKat.cleaned_data.get('sortMetoda') #sortiranje
            if odabranaOpcija == '1':
                proizvodi = proizvodi.order_by('-cena')
            elif odabranaOpcija == '2':
                proizvodi = proizvodi.order_by('cena')

        if formSearch.is_valid():
            tekstPretrage = formSearch.cleaned_data.get('searchField')
            if tekstPretrage != '':
                proizvodi = proizvodi.filter(naziv__icontains=tekstPretrage)
            print(proizvodi)
    else:
        formKat = FilterProductsKategorijaForm(categories=kategorije)
        formSearch = SearchForm()

    context = {
        'proizvodi': proizvodi,
        'formaKategorije': formKat,
        'jedanProizvod':jedanProizvod,
        'formaSearch':formSearch
    }
    return render(request, 'proizvodi.html', context)

# prikaz zaposlenih - TIJANA DJUKIC
# sortiranje zaposlenih - TIJANA DJUKIC
# pretraga zaposlenih - TIJANA DJUKIC
def prikazZaposlenih(request:HttpRequest): #*****NAPOMENA: ovde prikazati samo odobrene zaposlene*******
    jedanProizvod = ''
    zaposleni = Zaposleni.objects.all()
    zanimanja = Zaposleni.objects.values_list('zanimanje', flat=True).distinct()
    kategorije = [(zanimanje, zanimanje) for zanimanje in zanimanja]
    prosecneOcene = dict()

    # izracunavanje ocena
    for zap in Zaposleni.objects.all():
        oceneZaposlenog = Ocena.objects.filter(korisnik_id=zap.korisnik_id)
        prosek = oceneZaposlenog.aggregate(average=Avg('ocena'))['average']
        if prosek is not None:
            prosecneOcene[zap.korisnik_id] = str(prosek)
            zap.ocena = prosek
        else:
            prosecneOcene[zap.korisnik_id] = 0.0
            zap.ocena = 0
        zap.save()

    if request.method == 'POST':
        formKat = FilterProductsKategorijaForm(request.POST, categories=kategorije)
        formSearch = SearchForm(request.POST)

        if formKat.is_valid():  # izvlacenje proizvoda po odabranim kategorijama
            odabraneKategorije = formKat.cleaned_data.get('kategorije')
            print(odabraneKategorije)
            if odabraneKategorije:
                # odabraneKategorijeId = Kategorija.objects.filter(zanimanje__in=odabraneKategorije).values_list('idkat',
                #                                                                                            flat=True)
                zaposleni = Zaposleni.objects.filter(zanimanje__in=odabraneKategorije)


            odabranaOpcija = formKat.cleaned_data.get('sortMetoda')  # sortiranje
            if odabranaOpcija == '1':
                zaposleni = zaposleni.order_by('-ocena')
            elif odabranaOpcija == '2':
                zaposleni = zaposleni.order_by('ocena')

        if formSearch.is_valid():
            tekstPretrage = formSearch.cleaned_data.get('searchField')
            print(tekstPretrage)
            if tekstPretrage != '':
                zaposleni = zaposleni.filter(imeprezime__icontains=tekstPretrage)
    else:
        formKat = FilterProductsKategorijaForm(categories=kategorije)
        formSearch = SearchForm()

    context = {
        'zaposleni': zaposleni,
        'formaKategorije': formKat,
        'formaSearch': formSearch,
        'ocene':prosecneOcene
    }
    return render(request, 'zaposleni.html', context)

# prikaz najboljeg radnika i poslednjeg dodatog proizvoda - TIJANA DJUKIC
def index(request: HttpRequest):
    poslednjiDodatProizvod = Proizvod.objects.order_by('-idp').first()
    idKategorije = poslednjiDodatProizvod.kategorija_idkat.idkat
    print(idKategorije)
    kategorijaProizvoda = Kategorija.objects.all()
    kategorijaProizvoda=kategorijaProizvoda.filter(idkat= idKategorije).first()

    najboljeOcenjenZaposleni = Zaposleni.objects.order_by('-ocena').first()

    context={
        'proizvod':poslednjiDodatProizvod,
        'kategorija':kategorijaProizvoda,
        'zaposleni':najboljeOcenjenZaposleni
    }
    return render(request, 'index.html', context)

def jedanProizvod(request: HttpRequest):
    return render(request, 'jedanProizvod.html', dict())

# login -> JOVAN JOVOVIC
def login(request):
    if request.method == 'POST':
        korisnickoime = request.POST['username']
        lozinka = request.POST['password']

        try:
            korisnik = Korisnik.objects.get(korisnickoime=korisnickoime)
            if korisnik.lozinka == lozinka:
                # Ovde možete dodati kod za login sesiju ili preusmeravanje
                request.session['korid'] = korisnik.id
                return redirect('index')  # Zamenite 'home' sa nazivom vaše početne strane
            else:
                return HttpResponse("Pogrešna lozinka")
        except Korisnik.DoesNotExist:
            adminUser = Admin.objects.get(korisnickoime=korisnickoime, lozinka=lozinka)
            if adminUser:
                request.session['korid'] = 1
                request.session['admin'] = 'true'
                return redirect('index')

            return HttpResponse("Korisnik ne postoji")

    return render(request, 'login.html')

# odjava - TIJANA DJUKIC
def logout(request:HttpRequest):
    if 'korid' in request.session:
        del request.session['korid']
    if 'admin' in request.session:
        del request.session['admin']
    return redirect('login')

def korpa(request: HttpRequest):
    return render(request, 'korpa.html', dict())

#cenovnik - TIJANA DJUKIC
def cenovnik(request: HttpRequest):
    tretmani = Tretman.objects.all()
    context = {
        'tretmani':tretmani
    }
    return render(request, 'cenovnik.html', context)

def musterije(request: HttpRequest):
    return render(request, 'musterije.html', dict())

# isplacivanje plate zaposlenima - TIJANA DJUKIC
# zakazivanje termina - TIJANA DJUKIC
def nalog(request: HttpRequest): #*****NAPOMENA: ovde onemoguciti isplatu plate u slucaju da bi po isplati budzet bio manji od 0*****
    # if not request.user.is_authenticated:
    #     return redirect('login')
    idKor = request.session.get('korid')
    print(idKor)
    if idKor is None:
        return redirect('login')
    idKor = int(idKor)

    # pocetak meseca -> oznacavanje da plate zaposlenima nisu isplacene
    danasnjiDan = date.today().day
    if danasnjiDan == 1:
        for zaposleni in Zaposleni.objects.all():
            if zaposleni.odobren != 0:
                zaposleni.odobren = 1
                zaposleni.save()

    dropZaposleniOptions = [(obj.idz, obj.imeprezime) for obj in Zaposleni.objects.all().filter(odobren=1)] #biranje zaposlenih kojima plata jos uvek nije isplacena

    # deo za ocenjivanje prethodne usluge
    mojIdKorisnik = request.session.get('korid')
    korisnik = Korisnik.objects.get(id=mojIdKorisnik)
    zaposleniOcena = None
    muster = None
    poslednji_termin = None

    if Zaposleni.objects.filter(korisnik=mojIdKorisnik).exists():
        # ima dugme za potvrdu i ocenjuje musteriju
        # muster mi je ceo korisnik
        zaposleni = Zaposleni.objects.get(korisnik=mojIdKorisnik)
        rezervacijeOcena = Rezervacija.objects.filter(zaposleni_idz=zaposleni.idz).order_by('-idrez')

        poslednji_termin = next((rez for rez in rezervacijeOcena if rez.ostvaren == 0 and rez.ocenamusterija == 0),
                                None)

        if poslednji_termin:
            print('nasao poslednji termin')
            musterijaOcena = poslednji_termin.musterija_idm
            musterId = musterijaOcena.idm
            korTerminId = Musterija.objects.get(idm = musterId).korisnik.id
            muster = Korisnik.objects.get(id=korTerminId)
            zaposleniOcena = None
        else:
            muster = None

    elif Musterija.objects.filter(korisnik=mojIdKorisnik).exists():
        # klasican prikaz
        print('musterija sam')
        musterija = Musterija.objects.get(korisnik=mojIdKorisnik)
        rezervacijeOcena = Rezervacija.objects.filter(musterija_idm=musterija.idm).order_by('-idrez')

        poslednji_termin = next((rez for rez in rezervacijeOcena if rez.ostvaren == 1 and rez.ocenazap == 0), None)

        if poslednji_termin:
            zaposleniOcena = poslednji_termin.zaposleni_idz
            muster = None
        else:
            zaposleniOcena = None


    # potrebno za formu za zakazivanje termina
    dropTretmaniOption = [(obj.idt, obj.naziv) for obj in Tretman.objects.all()]
    radioZaposleniOptions = [(str(obj.zanimanje) + ' - ' + str(obj.idz), obj.imeprezime) for obj in Zaposleni.objects.all()]

    # popunjavanje kartice sa zakazanim terminima ----> ******NAPOMENA: POTREBNO JE OVDE DODATI TRENUTNI user.id+kreirati za mene kao musteriju id ako ga nema******
    mojIdKor = idKor
    mojIdMusterije = Musterija.objects.filter(korisnik_id=mojIdKor).first()
    if mojIdMusterije is None:
        try:
            prevId = Musterija.objects.last().idm
            mojIdMusterije = Musterija(korisnik_id=mojIdKor, idm=prevId + 1)
            mojIdMusterije.save()
            mojIdMusterije = mojIdMusterije.idm
        except IntegrityError as e:
            return HttpResponse(f'Error creating Musterija: {e}')
    else:
        mojIdMusterije = mojIdMusterije.idm
    mojeRezervacije = Rezervacija.objects.filter(musterija_idm=mojIdMusterije, ostvaren=0)
    tretman_ids = mojeRezervacije.values_list('tretman_idt', flat=True)
    mojiTretmani = Tretman.objects.filter(idt__in=tretman_ids)
    print(mojiTretmani)
    if request.method == 'POST':
        dropZaposleni = DropboxZaposleni(data=request.POST, zaposleni_choices=dropZaposleniOptions)
        formOcena = OcenaForm(data = request.POST)
        formaZakazivanje = zakazivanjeDan(data=request.POST, tretmani_choices=dropTretmaniOption, zaposleni_choices=radioZaposleniOptions)
        if dropZaposleni.is_valid():
            idZaposlenog=dropZaposleni.cleaned_data.get('zaposleni')
            odabraniZaposleni = Zaposleni.objects.all().filter(idz=idZaposlenog).first()
            zaIsplatu = odabraniZaposleni.plata
            if odabraniZaposleni.bonus == 1:
                zaIsplatu *= 1.1
            odabraniZaposleni.odobren = 2
            odabraniZaposleni.save()
            budzet = Budzetsalona.objects.first()
            if (budzet.ukupanbudzet -zaIsplatu) < 0:
                return HttpResponse('Nema dovoljno novca u kasi!')
            budzet.ukupanbudzet -= zaIsplatu
            budzet.save()
            dropZaposleniOptions = [(obj.idz, obj.imeprezime) for obj in Zaposleni.objects.all().filter(odobren=1)]
            dropZaposleni = DropboxZaposleni(zaposleni_choices=dropZaposleniOptions)
        if formOcena.is_valid():
            musterija_termin = request.POST.get('musterija_termin')
            ocena = formOcena.cleaned_data['ocena']

            request.session['musterija_termin'] = musterija_termin
            request.session['muster_id'] = muster.id if muster else None
            request.session['poslednji_termin_id'] = poslednji_termin.idrez if poslednji_termin else None
            request.session['zaposleniOcena_id'] = zaposleniOcena.idz if zaposleniOcena else None
            request.session['ocena'] = ocena
            print(
                f"Redirecting to nalogOcena with muster_id: {muster.id if muster else None}, dosao:{musterija_termin} poslednji_termin_id: {poslednji_termin.idrez if poslednji_termin else None}, zaposleniOcena_id: {zaposleniOcena.idz if zaposleniOcena else None}, ocena: {ocena}")
            return redirect('nalogOcena')
        if formaZakazivanje.is_valid():
            cleaned_data = formaZakazivanje.cleaned_data
            cleaned_data['datum'] = cleaned_data['datum'].isoformat()
            request.session['data'] = cleaned_data
            return redirect('proba1')
    else:
        dropZaposleni = DropboxZaposleni(zaposleni_choices=dropZaposleniOptions)
        formOcena = OcenaForm()
        formaZakazivanje = zakazivanjeDan(tretmani_choices=dropTretmaniOption, zaposleni_choices=radioZaposleniOptions)

    budzet = Budzetsalona.objects.first()
    adminje=''
    if 'admin' in request.session:
        adminje = '1'

    context = {
        'budzet':budzet,
        'dropZaposleni':dropZaposleni,
        'izmeni':'',
        'zaposleni' :zaposleniOcena,
        'formOcena':formOcena,
        'formaZakazivanje':formaZakazivanje,
        'mojeRezervacije':mojeRezervacije,
        'mojiTretmani':mojiTretmani,
        'korisnik':korisnik,
        'muster':muster,
        'poslednji_termin':poslednji_termin,
        'adminje':adminje
    }
    return render(request, 'nalog.html', context)

def oNama(request: HttpRequest):
    if 'korid' in request.session:
        del request.session['korid']
    if 'admin' in request.session:
        del request.session['admin']
    return render(request, 'oNama.html', dict())

# ocenjivanje prethodne usluge - DUNJA COLIC
def nalogOcena(request):
    # probaj ovo
    muster_id = request.session.get('muster_id')
    poslednji_termin_id = request.session.get('poslednji_termin_id')
    zaposleniOcena_id = request.session.get('zaposleniOcena_id')
    musterija_termin = request.session.get('musterija_terimn')
    ocena = request.session.get('ocena')

    print(f"nalogOcena view: muster_id={muster_id}, dosao:{musterija_termin} poslednji_termin_id={poslednji_termin_id}, zaposleniOcena_id={zaposleniOcena_id}, ocena={ocena}")

    poslednji_termin = Rezervacija.objects.get(idrez=poslednji_termin_id)

    if poslednji_termin:
        if muster_id:
            muster = Korisnik.objects.get(id=muster_id)
            # oceni musteriju
            poslednji_termin.ostvaren = 1
            poslednji_termin.ocenamusterija = ocena
            poslednji_termin.save()

            Ocena.objects.create(
                ocena=ocena,
                korisnik_id=muster.id
            )
        elif zaposleniOcena_id:
            zaposleniOcena = Zaposleni.objects.get(idz=zaposleniOcena_id)
            # oceni zaposlenog
            poslednji_termin.ocenazap = ocena
            poslednji_termin.save()

            zaposleniOcena.ocena = ocena
            zaposleniOcena.save()

            Ocena.objects.create(
                ocena=ocena,
                korisnik_id=zaposleniOcena.idz
            )

    return redirect('nalog')

# registracija - JOVAN JOVOVIC
def registracija(request):
    if request.method=='POST':
        ime = request.POST['ime']
        prezime = request.POST['prezime']
        korisnickoime = request.POST['username']
        email = request.POST['e-mail']
        telefon = request.POST['telefon']
        lozinka = request.POST['lozinka']
        lozinka_potvrda = request.POST['lozinka-potvrda']
        sig_pitanje = request.POST['drop-sig-pitanje']
        odg_na_pitanje = request.POST['sig-odgovor']

        if Korisnik.objects.filter(korisnickoime=korisnickoime).exists():
            return HttpResponse("Korisnicko ime vec postoji")

        if lozinka==lozinka_potvrda:
            # lozinka_heširana = make_password(lozinka)
            try:
                korisnik = Korisnik(
                    korisnickoime=korisnickoime,
                    lozinka=lozinka,
                    email=email,
                    sig_pitanje=sig_pitanje,
                    odg_na_pitanje=odg_na_pitanje,
                    telefon=telefon
                )
                korisnik.save()
                return redirect('login')
            except Exception as e:
                return HttpResponse(f"Greska pri registraciji: {e}")
        else:
            return HttpResponse("Lozinke se ne poklapaju. Pokusajte ponovo")
    return render(request, 'registracija.html')

# registracija zaposleni - JOVAN JOVOVIC
def registracijaZaposleni(request):
    if request.method == 'POST':
        # Dobijanje podataka iz request.POST
        ime = request.POST.get('ime')
        prezime = request.POST.get('prezime')
        zanimanje = request.POST.get('zanimanje')
        korisnickoime = request.POST.get('korisnickoime')  # Dodato za korisničko ime
        email = request.POST.get('email')
        telefon = request.POST.get('telefon')
        lozinka = request.POST.get('lozinka')
        lozinka_potvrda = request.POST.get('lozinka-potvrda')
        sig_pitanje = request.POST.get('drop-sig-pitanje')
        odgovor = request.POST.get('odgovor')  # Pretpostavka da je odgovor u polju lozinka-potvrda
        slika = request.FILES.get('slika')

        # Kreiranje korisnika
        try:
            korisnik = Korisnik(
                korisnickoime=korisnickoime,
                lozinka=lozinka,
                email=email,
                sig_pitanje=sig_pitanje,
                odg_na_pitanje=odgovor,
                telefon=telefon
            )
            korisnik.save()
            max_id = Zaposleni.objects.aggregate(Max('idz'))['idz__max']
            if max_id is None:
                max_id = 0
            else:
                max_id += 1

            zaposleni = Zaposleni(
                korisnik=korisnik,
                idz=max_id,
                imeprezime=ime + " " + prezime,
                zanimanje=zanimanje,
                bonus=0,
                odobren=0,
                plata=0,
                slika=slika
            )
            zaposleni.save()
            putanjaFoldera = r'C:\Users\tijan\OneDrive\Documents\fakultet\3. godina\PSI\PSI_PROJEKAT_FINALNO\tasha\static\images\zaposleni'
            naziv_fajla = slika.name
            putanja_fajla = os.path.join(putanjaFoldera, naziv_fajla)

            with open(putanja_fajla, 'wb+') as destinacija:
                for chunk in slika.chunks():
                    destinacija.write(chunk)

            max_id = Raspored.objects.aggregate(Max('idras'))['idras__max']
            if max_id is None:
                max_id = 0
            else:
                max_id += 1
            raspored = Raspored(
                idras=max_id,
                brojradnihdana=5,
                zaposleni_idz=zaposleni
            )
            raspored.save()
            idRasporeda = raspored.idras

            for i in range(1, 6):
                radnidan = Radnidan(
                    idrd=idRasporeda * 10 + i,
                    brojslobtermina=8,
                    raspored_idras=raspored
                )
                radnidan.save()

                idRadnogDana = radnidan.idrd
                for i in range(1, 9):
                    if i == 1:
                        v = "08:00:00"
                    elif i == 2:
                        v = "09:00:00"
                    elif i == 3:
                        v = "10:00:00"
                    elif i == 4:
                        v = "11:00:00"
                    elif i == 5:
                        v = "12:00:00"
                    elif i == 6:
                        v = "13:00:00"
                    elif i == 7:
                        v = "14:00:00"
                    else:
                        v = "15:00:00"

                    slobodantermin = Slobodantermin(
                        slobodan=1,
                        vreme=v,
                        radnidan_idrd=radnidan,
                        idst=idRadnogDana * 10 + i
                    )
                    slobodantermin.save()

            return redirect('login')
        except Exception as e:
            return HttpResponse(f"Greska pri registraciji: {e}")

        # Redirekcija na neku drugu stranicu nakon registracije
        return redirect('login')

    return render(request, 'registracijaZaposleni.html')


#zakazivanje termina - biranje vremena - TIJANA DJUKIC
def proba1(request: HttpRequest):
    if 'data' not in request.session:
        return HttpResponse('Nema sacuvanih podataka u sesiji!')

    sessionData = request.session['data']
    idTre = int(sessionData['tretmani'])
    print('id tretmana '+ str(idTre))
    idZap = int(sessionData['zaposleniZak'].split(' - ')[1])
    datum = sessionData['datum']
    datum = datetime.fromisoformat(datum).date()
    mojDan = None #OVO MOZDA NIJE OKEJ

    slobodniTermini=''
    for raspored in Raspored.objects.filter(zaposleni_idz=idZap):
        for dan in Radnidan.objects.filter(raspored_idras=raspored.idras):
            if dan.datum == datum:
                if dan.brojslobtermina > 0:
                    slobodniTermini = Slobodantermin.objects.filter(radnidan_idrd=dan.idrd, slobodan=1)
                    mojDan = dan

                else:
                    return HttpResponse('Nema slobodnih termina tog dana')

    #OVDE MOZDA PROVERA DA LI POSTOJE SLOBODNI TERMINI UOPSTE
    terminiOptions = [(ter.idst, ter.vreme) for ter in slobodniTermini]
    potvrda = ''
    if request.method == 'POST':
        forma = formaTermini(request.POST, termini_choices=terminiOptions)
        if forma.is_valid():
            odabranTerminId = forma.cleaned_data['termini']
            #podesavanje da termin vise nije slobodan
            termin = Slobodantermin.objects.filter(idst=odabranTerminId).first()
            termin.slobodan = 0
            termin.save()
            mojDan.brojslobtermina -= 1
            mojDan.save()
            #popunjavanje rezervacije
            zaposleni_instance = Zaposleni.objects.get(idz=idZap)
            tretman_instance = Tretman.objects.get(idt=idTre)
            korId = int(request.session.get('korid'))
            musterija_instance = Musterija.objects.get(korisnik_id=korId)

            novaRezervacija = Rezervacija(zaposleni_idz=zaposleni_instance, musterija_idm = musterija_instance, tretman_idt=tretman_instance, vreme=termin.vreme, ostvaren=0, datum=datum, ocenazap=0, ocenamusterija=0) #*****HARDCODOVANA MUSTERIJA********
            novaRezervacija.save()

            request.session['vreme'] = str(termin.vreme)
            request.session['datum'] = str(datum)
            request.session['tretman'] = Tretman.objects.get(idt=idTre).naziv

            return redirect('send_html_email', idrez=novaRezervacija.idrez)
    else:
        forma = formaTermini(termini_choices=terminiOptions)

    #---deo za popunjavanje osnovne stranice---
    mojIdKor = 1
    mojIdMusterije = Musterija.objects.filter(korisnik_id=mojIdKor).first().idm
    mojeRezervacije = Rezervacija.objects.filter(musterija_idm=mojIdMusterije, ostvaren=0)
    tretman_ids = mojeRezervacije.values_list('tretman_idt', flat=True)
    mojiTretmani = Tretman.objects.filter(idt__in=tretman_ids)
    musterijaOcena = Musterija.objects.get(korisnik=2)
    rezervacijeOcena = Rezervacija.objects.filter(musterija_idm=musterijaOcena.idm).order_by('-idrez')

    poslednji_termin = next((rez for rez in rezervacijeOcena if rez.ostvaren == 1 and rez.ocenazap == 0), None)

    if poslednji_termin:
        zaposleniOcena = poslednji_termin.zaposleni_idz
    else:
        zaposleniOcena = None
    dropZaposleniOptions = [(obj.idz, obj.imeprezime) for obj in Zaposleni.objects.all().filter(
        odobren=1)]  # biranje zaposlenih kojima plata jos uvek nije isplacena
    dropTretmaniOption = [(obj.idt, obj.naziv) for obj in Tretman.objects.all()]
    radioZaposleniOptions = [(str(obj.zanimanje) + ' - ' + str(obj.idz), obj.imeprezime) for obj in
                             Zaposleni.objects.all()]
    dropZaposleni = DropboxZaposleni(zaposleni_choices=dropZaposleniOptions)
    formOcena = OcenaForm()
    formaZakazivanje = zakazivanjeDan(tretmani_choices=dropTretmaniOption, zaposleni_choices=radioZaposleniOptions)
    budzet = Budzetsalona.objects.first()
    context = {
        'budzet': budzet,
        'dropZaposleni': dropZaposleni,
        'izmeni': '',
        'zaposleni': zaposleniOcena,
        'formOcena': formOcena,
        'formaZakazivanje': formaZakazivanje,
        'mojeRezervacije': mojeRezervacije,
        'mojiTretmani': mojiTretmani,
        'potvrda': potvrda,
        'forma':forma
    }

    return render(request, 'proba1.html', context)

# dodavanje omiljenih - JANKO DOSEV
def add_to_favorites(request, idp):
    proizvod = get_object_or_404(Proizvod, idp=int(idp))
    print({'proizvod':idp})
    try:
        idKor = request.session.get('korid')
        if idKor is None:
            return HttpResponse('Niste ulogovani!')
        idKor = int(idKor)
        korisnik_proizvod, created = KorisnikHasProizvod.objects.get_or_create(korisnik_id=idKor, proizvod_idp=proizvod)
        if created:
            messages.success(request, "Proizvod je uspešno dodat u omiljene.")
        else:
            messages.info(request, "Proizvod je već u omiljenim.")
    except Exception as e:
        messages.error(request, "Došlo je do greške prilikom dodavanja u omiljene.")
        print(e)
    return redirect('proizvodi')

# otkazivanje termina - TIJANA DJUKIC
def otkazivanjeTermina(request, idrez):
    rezervacija = get_object_or_404(Rezervacija, idrez=int(idrez))
    idZaposleni = rezervacija.zaposleni_idz
    datum = rezervacija.datum
    vreme = rezervacija.vreme

    raspored = Raspored.objects.filter(zaposleni_idz=idZaposleni).first()
    idRasporeda = raspored.idras

    radnidan = Radnidan.objects.filter(datum=datum, raspored_idras=idRasporeda).first()
    radnidan.brojslobtermina += 1
    radnidanId = radnidan.idrd
    radnidan.save()

    slobodantermin = Slobodantermin.objects.filter(radnidan_idrd=radnidanId, vreme=vreme).first()
    slobodantermin.slobodan = 1
    slobodantermin.save()

    rezervacija.delete()

    return redirect('nalog')

# provera da li je potrebno obrisati termin - TIJANA DJUKIC
def proveraBrisanjaTermina(request, idrez):
    mojIdKor = int(request.session.get('korid'))
    mojIdMusterije = Musterija.objects.filter(korisnik_id=mojIdKor).first().idm
    mojeRezervacije = Rezervacija.objects.filter(musterija_idm=mojIdMusterije, ostvaren=0)
    tretman_ids = mojeRezervacije.values_list('tretman_idt', flat=True)
    mojiTretmani = Tretman.objects.filter(idt__in=tretman_ids)
    musterijaOcena = Musterija.objects.get(korisnik=2)
    rezervacijeOcena = Rezervacija.objects.filter(musterija_idm=musterijaOcena.idm).order_by('-idrez')

    poslednji_termin = next((rez for rez in rezervacijeOcena if rez.ostvaren == 1 and rez.ocenazap == 0), None)

    if poslednji_termin:
        zaposleniOcena = poslednji_termin.zaposleni_idz
    else:
        zaposleniOcena = None

    dropZaposleniOptions = [(obj.idz, obj.imeprezime) for obj in Zaposleni.objects.all().filter(odobren=1)] #biranje zaposlenih kojima plata jos uvek nije isplacena
    dropTretmaniOption = [(obj.idt, obj.naziv) for obj in Tretman.objects.all()]
    radioZaposleniOptions = [(str(obj.zanimanje) + ' - ' + str(obj.idz), obj.imeprezime) for obj in Zaposleni.objects.all()]
    dropZaposleni = DropboxZaposleni(zaposleni_choices=dropZaposleniOptions)
    formOcena = OcenaForm()
    formaZakazivanje = zakazivanjeDan(tretmani_choices=dropTretmaniOption, zaposleni_choices=radioZaposleniOptions)
    budzet = Budzetsalona.objects.first()
    context = {
        'budzet': budzet,
        'dropZaposleni': dropZaposleni,
        'izmeni': '',
        'zaposleni': zaposleniOcena,
        'formOcena': formOcena,
        'formaZakazivanje': formaZakazivanje,
        'mojeRezervacije': mojeRezervacije,
        'mojiTretmani': mojiTretmani,
        'idrez':idrez,
        'potvrda':''
    }
    return render(request, 'proveraBrisanjaTermina.html', context)

# uklanjnanje omiljenih - JANKO DOSEV
def remove_from_favorites(request, idp):
    print(idp)
    proizvod = get_object_or_404(Proizvod, idp=idp)
    try:
        idKor = request.session.get('korid')
        if idKor is None:
            return HttpResponse('Niste ulogovani!')
        idKor = int(idKor)
        idp = int(idp)
        korisnik_proizvod = KorisnikHasProizvod.objects.get(korisnik_id=idKor, proizvod_idp=idp)
        korisnik_proizvod.delete()
        messages.success(request, "Proizvod je uspešno uklonjen iz omiljenih.")
    except KorisnikHasProizvod.DoesNotExist:
        messages.error(request, "Proizvod nije pronađen u omiljenim.")
    except Exception as e:
        messages.error(request, "Došlo je do greške prilikom uklanjanja iz omiljenih.")
        print(e)
    return redirect('omiljeno')

# prikaz omiljenih - JANKO DOSEV
def omiljeno_view(request):
    idKor = request.session.get('korid')

    if idKor is not None:
        idKor = int(idKor)
        favorites = KorisnikHasProizvod.objects.filter(korisnik_id=idKor)
        context = {'favorites': favorites}
        return render(request, 'omiljeno.html', context)
    else:
        return HttpResponse('Niste ulogovani!')

from django.core.mail import send_mail
from django.core.mail import send_mail
from django.template.loader import get_template
# from django.utils.html import strip_tags
# from django.conf import settings

# slanje mejla za potvrdu zakazanog termina - TIJANA DJUKIC
def send_html_email(request, idrez):
    subject = 'Zakazivanje termina'
    message = 'Here is the message.'

    vreme = request.session['vreme']
    datum = request.session['datum']
    tretman = request.session['tretman']

    context = {
        'datum': datum,
        'vreme': vreme,
        'tretman': tretman,
        'idrez':idrez
    }

    template = get_template('mejlTemplate.html')
    html_content = template.render(context)
    html_message = html_content

    idKor = int(request.session.get('korid'))
    mojKorisnik = Korisnik.objects.filter(id=idKor).first()

    from_email = 'salonlepotetasa2024@gmail.com'
    to_email = mojKorisnik.email # ***********NAPOMENA: ovde staviti mejl korisnika!!!!***************

    send_mail(subject, message, from_email, [to_email], html_message=html_message)
    return redirect('nalog')

# izmena korisnickog imena - DUNJA COLIC
def izmenaKorime(request: HttpRequest):
    if request.method == 'POST':
        korisnickoime = request.POST['username']
        mojIdKorisnik = request.session.get('korid')
        print(mojIdKorisnik)

        if mojIdKorisnik:
            korisnik = Korisnik.objects.get(id=mojIdKorisnik)

            if Korisnik.objects.filter(korisnickoime=korisnickoime).exists():
                return HttpResponse("Korisnicko ime vec postoji")

            korisnik.korisnickoime = korisnickoime
            korisnik.save()
            return HttpResponse("Korisnicko ime je uspesno promenjeno")
        else:
            return HttpResponse("Niste prijavljeni")

    context = {}
    return render(request, 'izmenaKorime.html', context)

# izmena email adrese - DUNJA COLIC
def izmenaEmail(request: HttpRequest):
    if request.method == 'POST':
        email = request.POST['email']
        mojIdKorisnik = request.session.get('korid')
        print(mojIdKorisnik)

        if mojIdKorisnik:
            korisnik = Korisnik.objects.get(id=mojIdKorisnik)

            if Korisnik.objects.filter(email=email).exists():
                return HttpResponse("Email se vec koristi")

            korisnik.email = email
            korisnik.save()
            return HttpResponse("Email je uspesno promenjen")
        else:
            return HttpResponse("Niste prijavljeni")

    context = {}
    return render(request, 'izmenaEmail.html', context)

# izmena telefona - DUNJA COLIC
def izmenaTelefon(request: HttpRequest):
    if request.method == 'POST':
        telefon = request.POST['telefon']
        mojIdKorisnik = request.session.get('korid')

        if mojIdKorisnik:
            korisnik = Korisnik.objects.get(id=mojIdKorisnik)

            if Korisnik.objects.filter(telefon=telefon).exists():
                return HttpResponse("Ovaj broj telefona se vec koristi")

            korisnik.telefon = telefon
            korisnik.save()
            return HttpResponse("Broj telefona je uspesno promenjen")
        else:
            return HttpResponse("Niste prijavljeni")

    context = {}
    return render(request, 'izmenaTelefon.html', context)

# izmena lozinke - DUNJA COLIC
def izmenaLozinka(request):
    if request.method=='POST':
        mojIdKorisnik = request.session.get('korid')
        stara = request.POST['stara']
        nova = request.POST['nova']
        potvrda = request.POST['potvrda']

        if mojIdKorisnik:
            korisnik = Korisnik.objects.get(id=mojIdKorisnik)

            if korisnik.lozinka != stara:
                return HttpResponse("Pogresna stara lozinka")

            if nova != potvrda:
                return HttpResponse("Ispravno unesite potvrdu nove lozinke!")

            korisnik.lozinka = nova
            korisnik.save()
            return HttpResponse("Lozinka je uspesno promenjena!")
        else:
            return HttpResponse("Niste prijavljeni")

    return render(request, 'izmenaLozinka.html')

# dodavanje u korpu - JANKO DOSEV
def add_to_cart(request, idp):
    proizvod = get_object_or_404(Proizvod, idp=idp)
    try:
        idKor = request.session.get('korid')
        if idKor is None:
            print("User not logged in")
            return HttpResponse('Niste ulogovani!')
        idKor = int(idKor)
        korisnik = get_object_or_404(Korisnik, id=idKor)
        print(f"Adding product {idp} to cart for user {idKor}")
        item, created = KorisnikImaProizvodZaKorpu.objects.get_or_create(
            korisnik=korisnik,
            proizvod=proizvod,
            defaults={'broj_proizvoda': 1, 'cena_ukupna': proizvod.cena}
        )

        if not created:
            item.broj_proizvoda += 1
            item.cena_ukupna = proizvod.cena * item.broj_proizvoda
            item.save()

        messages.success(request, "Proizvod je uspešno dodat u korpu.")
        print("Item added to cart")
    except Exception as e:
        messages.error(request, "Došlo je do greške prilikom dodavanja u korpu.")
        print("Error adding itefdfdfdfsm to cart:", e)

    return redirect('korpa')

# updateovanje korpe -JANKO DOSEV
def update_cart(request, idp, action):
    user_id = request.session.get('korid')
    if user_id is None:
        return redirect('login')  # Redirect to login if not logged in

    korisnik = get_object_or_404(Korisnik, id=user_id)
    item = get_object_or_404(KorisnikImaProizvodZaKorpu, korisnik=korisnik, proizvod__idp=idp)

    if action == 'increase':
        item.broj_proizvoda += 1
    elif action == 'decrease' and item.broj_proizvoda > 1:
        item.broj_proizvoda -= 1

    item.cena_ukupna = item.broj_proizvoda * item.proizvod.cena
    item.save()

    return redirect('korpa')

# pregled korpe - JANKO DOSEV
def cart_view(request):
    user_id = request.session.get('korid')
    if user_id is None:
        return redirect('login')  # Redirect to login if not logged in

    korisnik = get_object_or_404(Korisnik, id=user_id)
    cart_items = KorisnikImaProizvodZaKorpu.objects.filter(korisnik=korisnik)
    total_price = sum(item.cena_ukupna for item in cart_items)

    print("Cart Items:", cart_items)
    print("Total Price:", total_price)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'korpa.html', context)


from django.http import JsonResponse
from django.utils import timezone

# finisiranje porudzbine - JANKO DOSEV
def finalize_order(request):
    user_id = request.session.get('korid')
    if user_id is None:
        return redirect('login')  # Redirect to login if not logged in

    korisnik = get_object_or_404(Korisnik, id=user_id)
    cart_items = KorisnikImaProizvodZaKorpu.objects.filter(korisnik=korisnik)
    total_price = sum(item.cena_ukupna for item in cart_items)

    discount_code = request.POST.get('discount_code')
    discount_feedback = ""
    discount_feedback_class = ""
    discount = 0
    if discount_code:
        try:
            popust = Popusti.objects.get(kod_popusta=discount_code)
            discount = popust.procenat
            total_price -= int(total_price * (discount // 100))
            discount_feedback = "Kod za popust je dobar"
            discount_feedback_class = "text-success"
        except Popusti.DoesNotExist:
            discount_feedback = "Kod za popust je loÅ¡"
            discount_feedback_class = "text-danger"

    shipping_method = request.POST.get('postarina')
    shipping_cost = 0
    if shipping_method == "Standardna- 200.00din":
        shipping_cost = 200

    total_price += shipping_cost

    # Create the Narudzbina object
    mojIdMusterije = Musterija.objects.filter(korisnik_id=user_id).first()
    if mojIdMusterije is None:
        try:
            prevId = Musterija.objects.last().idm
            mojIdMusterije = Musterija(korisnik_id=user_id, idm=prevId + 1)
            mojIdMusterije.save()
            mojIdMusterije = mojIdMusterije.idm
        except IntegrityError as e:
            return HttpResponse(f'Error creating Musterija: {e}')
    else:
        mojIdMusterije = mojIdMusterije.idm
    musterija = get_object_or_404(Musterija, idm=mojIdMusterije)
    narudzbina = Narudzbina.objects.create(
        musterija_idm=musterija,
        ukupnacena=total_price,
        status=1,
        adresa=request.POST.get('adresa', ''),
        datum=timezone.now().date(),
        obradjena=0
    )

    # Add each item in the cart to the Narudzbina
    for item in cart_items:
        Narucenproizvod.objects.create(
            narudzbina_idnarudzbe=narudzbina,
            proizvod_idp=item.proizvod,
            kolicina=item.broj_proizvoda
        )
        item.delete()# Clear the cart after finalizing the order

    budzet = Budzetsalona.objects.first()
    if budzet:
        budzet.ukupanbudzet += total_price
        budzet.save()

    context = {
        'narudzbina': narudzbina,
        'narucenproizvodi': Narucenproizvod.objects.filter(narudzbina_idnarudzbe=narudzbina),
        'total_price': total_price,
        'discount_feedback': discount_feedback,
        'discount_feedback_class': discount_feedback_class,
        'shipping_cost': shipping_cost,
        'discount': discount,
        'has_items': cart_items.exists(),  # Add this line
    }

    return render(request, 'order_confirmation.html', context)

# provera koda za popust - JANKO DOSEV
def validate_discount_code(request):
    discount_code = request.GET.get('discount_code')
    response_data = {}
    try:
        popust = Popusti.objects.get(kod_popusta=discount_code)
        response_data = {
            'valid': True,
            'message': 'Kod za popust je dobar',
            'discount': popust.procenat
        }
    except Popusti.DoesNotExist:
        response_data = {
            'valid': False,
            'message': 'Kod za popust je loš'
        }
    return JsonResponse(response_data)

# zaposleni raspored - JOVAN JOVOVIC
def zaposleniRaspored(request):
    idKor = request.session.get('korid')
    print(idKor)
    if idKor is None:
        return redirect('login')
    idKor = int(idKor)
    korisnik = Korisnik.objects.get(id=idKor)


    id_zap = Zaposleni.objects.get(korisnik=korisnik).idz
    zaposleni = Zaposleni.objects.get(pk=id_zap)
    rezervacije = Rezervacija.objects.filter(zaposleni_idz=id_zap)
    lista_rezervacija = []

    for rez in rezervacije:
        podaci={
            'musterija': rez.musterija_idm.korisnik.korisnickoime,
            'email': rez.musterija_idm.korisnik.email,
            'tretman': rez.tretman_idt.naziv,
            'vreme': rez.vreme,
            'datum': rez.datum
        }
        lista_rezervacija.append(podaci)


    context = {
        'zaposleni': zaposleni,
        'rezervacije': lista_rezervacija,
    }
    return render(request, 'zaposleniRaspored.html', context)

def musterijaRaspored(request):
    idKor = request.session.get('korid')
    print(idKor)
    if idKor is None:
        return redirect('login')
    idKor = int(idKor)
    korisnik = Korisnik.objects.get(id=idKor)

    id_musterija = Musterija.objects.get(korisnik=korisnik).idm
    musterija = Musterija.objects.get(idm=id_musterija)
    rezervacije=Rezervacija.objects.filter(musterija_idm=id_musterija)
    lista_rezervacija=[]

    for rez in rezervacije:
        podaci={
            'zaposleni': rez.zaposleni_idz.imeprezime,
            'tretman': rez.tretman_idt.naziv,
            'vreme': rez.vreme,
            'datum': rez.datum
        }
        lista_rezervacija.append(podaci)

    context={
        'musterija': musterija,
        'rezervacije': lista_rezervacija
    }
    return render(request, 'musterijaRaspored.html', context)

def zaboravljena_lozinka_view(request):
    if request.method == "POST":
        korisnicko_ime = request.POST.get('username')
        try:
            korisnik = Korisnik.objects.get(korisnickoime=korisnicko_ime)
            print(korisnik.korisnickoime)
            print(korisnik.email)
            request.session['username'] = korisnik.korisnickoime
            return redirect('lozinka_pitanja')  # Koristite redirect umesto render
        except Korisnik.DoesNotExist:
            return HttpResponse("Bad Username")

    return render(request, 'zaboravljena_lozinka1.html')


def lozinka_pitanja_view(request):
    username = request.session.get('username', 'Nema korisnickog imena')
    try:
        korisnik = Korisnik.objects.get(korisnickoime=username)
        sigurnosno_pitanje = korisnik.sig_pitanje
        odgovor_pravi = korisnik.odg_na_pitanje
    except Korisnik.DoesNotExist:
        return HttpResponse("Bad Username")

    if request.method == 'POST':
        odgovor = request.POST.get('odgovor')
        if odgovor_pravi == odgovor:
            return redirect('lozinka_promena')
        else:
            return redirect("lozinka_pitanja")

    return render(request, 'zaboravljena_lozinka2.html', {'sigurnosno_pitanje': sigurnosno_pitanje, 'username': username})

def lozinka_promena_view(request):
    username = request.session.get('username', 'Nema korisnickog imena')
    try:
        korisnik=Korisnik.objects.get(korisnickoime=username)
        print(korisnik.email)
    except Korisnik.DoesNotExist:
        return HttpResponse("Bad Username")

    if request.method == 'POST':
        lozinka1=request.POST.get('lozinka1')
        lozinka2=request.POST.get('lozinka2')
        print("Lozinka 1: "+lozinka1)
        print("Lozinka 2: "+lozinka2)
        print
        if lozinka1 == lozinka2:
            korisnik.lozinka = lozinka2  # Postavljanje nove lozinke
            print("Lozinka 1: "+lozinka1)
            print("Lozinka 2: "+lozinka2)
            print("Nova lozinka postavljena:", korisnik.lozinka)
            korisnik.save()  # Čuvanje promena u bazi podataka
            print("Korisnik sacuvan")
            return redirect('zaboravljena_lozinka_potvrda')
        else:
            return render(request, 'zaboravljena_lozinka_promena.html', {'username' : korisnik.korisnickoime})


    return render(request, 'zaboravljena_lozinka_promena.html', {'username' : korisnik.korisnickoime})


def lozinka_promena_potvrda(request):
    return render(request, 'zaboravljena_lozinka_potvrda.html')

def delete_from_cart(request, idp):
    user_id = request.session.get('korid')
    if user_id is None:
        return redirect('login')  # Redirect to login if not logged in

    korisnik = get_object_or_404(Korisnik, id=user_id)
    item = get_object_or_404(KorisnikImaProizvodZaKorpu, korisnik=korisnik, proizvod__idp=idp)

    item.delete()  # Remove the item from the cart

    return redirect('korpa')

def jedanProizvod(request: HttpRequest, idp):
    proiz = Proizvod.objects.get(idp=idp)
    proizvodi = Proizvod.objects.all()
    context = {
        'proiz':proiz,
        'proizvodi':proizvodi,
        'jedanProizvod':''
    }
    return render(request, 'jedanProizvod.html', context)


def pojedinacniZaposleni(request, idz):
    zaposleni = Zaposleni.objects.get(idz=idz)
    return render(request, 'pojedinacniZaposleni.html', {'zaposleni':zaposleni})

def prikazMogRasporeda(request):
    user_id = request.session.get('korid')
    if user_id is None:
        return redirect('login')

    if Zaposleni.objects.filter(korisnik=user_id).exists():
        return redirect('zaposleniRaspored')
    else:
        return redirect('musterijaRaspored')