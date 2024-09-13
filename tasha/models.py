
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):

    korisnickoime = models.CharField(db_column='KorisnickoIme', primary_key=True,
                                     max_length=45)  # Field name made lowercase.
    lozinka = models.CharField(db_column='Lozinka',
                               max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Budzetsalona(models.Model):
    idbudzetsalona = models.IntegerField(db_column='idBudzetSalona', primary_key=True)  # Field name made lowercase.
    ukupanbudzet = models.IntegerField(db_column='UkupanBudzet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'budzetsalona'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Kategorija(models.Model):
    idkat = models.AutoField(db_column='IdKat', primary_key=True)  # Field name made lowercase.
    naziv = models.CharField(db_column='Naziv', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kategorija'


class Korisnik(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    korisnickoime = models.CharField(db_column='KorisnickoIme', unique=True, max_length=45)  # Field name made lowercase.
    lozinka = models.CharField(db_column='Lozinka', max_length=45)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=45)
    sig_pitanje = models.CharField(db_column='Sig.pitanje', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    odg_na_pitanje = models.CharField(db_column='Odg_na_pitanje', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='Telefon', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'korisnik'


class KorisnikHasProizvod(models.Model):
    korisnik = models.OneToOneField(Korisnik, models.DO_NOTHING, db_column='Korisnik_Id',
                                    primary_key=True)  # Field name made lowercase. The composite primary key (Korisnik_Id, Proizvod_IdP) found, that is not supported.Thefirstolumn is selected. \
    proizvod_idp = models.ForeignKey('Proizvod', models.DO_NOTHING,
                                     db_column='Proizvod_IdP')  # Field name made lowercase.


class Meta:
    managed = False
    db_table = 'tasha_korisnikhasproizvod'
    unique_together = (('korisnik', 'proizvod_idp'),)


class Musterija(models.Model):
    idm = models.IntegerField(db_column='IdM', primary_key=True)  # Field name made lowercase.
    korisnik = models.OneToOneField(Korisnik, models.DO_NOTHING, db_column='Korisnik_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'musterija'


class Narucenproizvod(models.Model):
    narudzbina_idnarudzbe = models.OneToOneField('Narudzbina', models.DO_NOTHING, db_column='Narudzbina_IdNarudzbe',
                                                 primary_key=True)  # Field name made lowercase. The composite primarykey(Narudzbina_IdNarudzbe, Proizvod_IdP)found, that is not supported.Thefirstcolumn is selected.
    proizvod_idp = models.ForeignKey('Proizvod', models.DO_NOTHING, db_column='Proizvod_IdP')  # Field name made lowercase.
    kolicina = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'narucenproizvod'
        unique_together = (('narudzbina_idnarudzbe', 'proizvod_idp'),)


class Narudzbina(models.Model):
    """
        Ovo je klasa cija jedna instanca sadrzi informacije o jednoj narudzbini.
    """
    idnarudzbe = models.AutoField(db_column='IdNarudzbe', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    ukupnacena = models.CharField(db_column='UkupnaCena', max_length=45)  # Field name made lowercase.
    adresa = models.CharField(db_column='Adresa', max_length=45)  # Field name made lowercase.
    datum = models.DateField(db_column='Datum', blank=True, null=True)  # Field name made lowercase.
    musterija_idm = models.ForeignKey(Musterija, models.DO_NOTHING,
                                      db_column='Musterija_IdM')  # Field name made lowercase.
    obradjena = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'narudzbina'


class Ocena(models.Model):
    ido = models.AutoField(db_column='IdO', primary_key=True)  # Field name made lowercase.
    ocena = models.IntegerField()
    korisnik = models.OneToOneField(Korisnik, models.DO_NOTHING, db_column='Korisnik_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ocena'


class Popusti(models.Model):
    id_popusta = models.AutoField(primary_key=True)
    procenat = models.IntegerField()
    kod_popusta = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'popusti'


class Proizvod(models.Model):
    idp = models.AutoField(db_column='IdP', primary_key=True)  # Field name made lowercase.
    naziv = models.CharField(db_column='Naziv', max_length=100)  # Field name made lowercase.
    cena = models.IntegerField(db_column='Cena')  # Field name made lowercase.
    opis = models.CharField(db_column='Opis', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fiksnipopust = models.IntegerField(db_column='FiksniPopust', blank=True, null=True)  # Field name made lowercase.
    kategorija_idkat = models.ForeignKey(Kategorija, models.DO_NOTHING,
                                         db_column='Kategorija_IdKat')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proizvod'


class Radnidan(models.Model):
    idrd = models.AutoField(db_column='IdRD',
                            primary_key=True)  # Field name made lowercase. The composite primary key (IdRD, Raspored_IdRas) found, that is not supported. The firstcolumn is selected.
    brojslobtermina = models.IntegerField(db_column='BrojSlobTermina', blank=True, null=True)  # Field name made lowercase.
    raspored_idras = models.ForeignKey('Raspored', models.DO_NOTHING,db_column='Raspored_IdRas')  # Field name made lowercase.
    datum = models.DateField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'radnidan'
        unique_together = (('idrd', 'raspored_idras'),)


class Raspored(models.Model):
    idras = models.IntegerField(db_column='IdRas', primary_key=True)  # Field name made lowercase.
    brojradnihdana = models.IntegerField(db_column='BrojRadnihDana', blank=True,
                                         null=True)  # Field name made lowercase.
    zaposleni_idz = models.ForeignKey('Zaposleni', models.DO_NOTHING,
                                      db_column='Zaposleni_IdZ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'raspored'


class Rezervacija(models.Model):
    idrez = models.AutoField(db_column='IdRez',
                             primary_key=True)  # Field name made lowercase. The composite primary key (IdRez, Zaposleni_IdZ, Musterija_IdM) found, that is not supported.Thefirstcolumn is selected.
    zaposleni_idz = models.ForeignKey('Zaposleni', models.DO_NOTHING,
                                      db_column='Zaposleni_IdZ')  # Field name made lowercase.
    musterija_idm = models.ForeignKey(Musterija, models.DO_NOTHING, db_column='Musterija_IdM')  # Field name made lowercase.
    tretman_idt = models.ForeignKey('Tretman', models.DO_NOTHING, db_column='Tretman_IdT')  # Field name made lowercase.
    vreme = models.TimeField(db_column='Vreme')  # Field name made lowercase.
    ostvaren = models.IntegerField(db_column='Ostvaren', blank=True, null=True)  # Field name made lowercase.
    ocenazap = models.IntegerField(db_column='OcenaZap', blank=True, null=True)  # Field name made lowercase.
    ocenamusterija = models.IntegerField(db_column='OcenaMusterija', blank=True, null=True)  # Field name made lowercase.
    datum = models.DateField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'rezervacija'
        unique_together = (('idrez', 'zaposleni_idz', 'musterija_idm'),)


class Slobodantermin(models.Model):
    idst = models.AutoField(db_column='IdST', primary_key=True)  # Field name made lowercase.
    radnidan_idrd = models.ForeignKey(Radnidan, models.DO_NOTHING,
                                      db_column='RadniDan_IdRD')  # Field name made lowercase.
    vreme = models.TimeField(db_column='Vreme')  # Field name made lowercase.
    slobodan = models.IntegerField(db_column='Slobodan')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slobodantermin'


class Tretman(models.Model):
    idt = models.AutoField(db_column='IdT', primary_key=True)  # Field name made lowercase.
    naziv = models.CharField(db_column='Naziv', max_length=45)  # Field name made lowercase.
    opis = models.CharField(db_column='Opis', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cena = models.IntegerField(db_column='Cena')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tretman'


class Zaposleni(models.Model):
    idz = models.IntegerField(db_column='IdZ', primary_key=True)  # Field name made lowercase.
    imeprezime = models.CharField(db_column='ImePrezime', max_length=45)  # Field name made lowercase.
    zanimanje = models.CharField(db_column='Zanimanje', max_length=45)  # Field name made lowercase.
    bonus = models.IntegerField(db_column='Bonus', blank=True, null=True)  # Field name made lowercase.
    plata = models.IntegerField(db_column='Plata')  # Field name made lowercase.
    odobren = models.IntegerField(db_column='Odobren', blank=True, null=True)  # Field name made lowercase.
    korisnik = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='Korisnik_Id')  # Field name made lowercase.
    slika = models.CharField(max_length=300, blank=True, null=True)
    ocena = models.FloatField(db_column='Ocena', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'zaposleni'

    def str(self):
        return f"Ime i Prezime:{self.imeprezime} zanimanje:{self.zanimanje}"

class KorisnikImaProizvodZaKorpu(models.Model):
    korisnik = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='Korisnik_Id', )
    proizvod = models.ForeignKey(Proizvod, models.DO_NOTHING, db_column='Proizvod_IdP',  primary_key=True)
    broj_proizvoda = models.IntegerField(db_column='brojProizvoda')
    cena_ukupna = models.DecimalField(db_column='cenaUkupna', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tasha_korisnikimaproizvodzakorpu'
        unique_together = (('korisnik', 'proizvod'),)