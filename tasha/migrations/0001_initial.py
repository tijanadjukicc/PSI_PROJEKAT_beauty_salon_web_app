# Generated by Django 5.0.6 on 2024-05-28 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('korisnickoime', models.CharField(db_column='KorisnickoIme', max_length=45, primary_key=True, serialize=False)),
                ('lozinka', models.CharField(db_column='Lozinka', max_length=45)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Budzetsalona',
            fields=[
                ('idbudzetsalona', models.IntegerField(db_column='idBudzetSalona', primary_key=True, serialize=False)),
                ('ukupanbudzet', models.IntegerField(blank=True, db_column='UkupanBudzet', null=True)),
            ],
            options={
                'db_table': 'budzetsalona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kategorija',
            fields=[
                ('idkat', models.AutoField(db_column='IdKat', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', max_length=45)),
            ],
            options={
                'db_table': 'kategorija',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('korisnickoime', models.CharField(db_column='KorisnickoIme', max_length=45, unique=True)),
                ('lozinka', models.CharField(db_column='Lozinka', max_length=45)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('sig_pitanje', models.CharField(blank=True, db_column='Sig.pitanje', max_length=45, null=True)),
                ('odg_na_pitanje', models.CharField(blank=True, db_column='Odg_na_pitanje', max_length=45, null=True)),
                ('telefon', models.CharField(blank=True, db_column='Telefon', max_length=45, null=True)),
            ],
            options={
                'db_table': 'korisnik',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Musterija',
            fields=[
                ('idm', models.IntegerField(db_column='IdM', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'musterija',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Narudzbina',
            fields=[
                ('idnarudzbe', models.AutoField(db_column='IdNarudzbe', primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('ukupnacena', models.CharField(db_column='UkupnaCena', max_length=45)),
                ('adresa', models.CharField(db_column='Adresa', max_length=45)),
                ('datum', models.DateField(blank=True, db_column='Datum', null=True)),
                ('obradjena', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'narudzbina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('ido', models.AutoField(db_column='IdO', primary_key=True, serialize=False)),
                ('ocena', models.IntegerField()),
            ],
            options={
                'db_table': 'ocena',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Popusti',
            fields=[
                ('id_popusta', models.AutoField(primary_key=True, serialize=False)),
                ('procenat', models.IntegerField()),
                ('kod_popusta', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'popusti',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proizvod',
            fields=[
                ('idp', models.AutoField(db_column='IdP', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', max_length=100)),
                ('cena', models.IntegerField(db_column='Cena')),
                ('opis', models.CharField(blank=True, db_column='Opis', max_length=500, null=True)),
                ('fiksnipopust', models.IntegerField(blank=True, db_column='FiksniPopust', null=True)),
            ],
            options={
                'db_table': 'proizvod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Radnidan',
            fields=[
                ('idrd', models.AutoField(db_column='IdRD', primary_key=True, serialize=False)),
                ('brojslobtermina', models.IntegerField(blank=True, db_column='BrojSlobTermina', null=True)),
            ],
            options={
                'db_table': 'radnidan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Raspored',
            fields=[
                ('idras', models.IntegerField(db_column='IdRas', primary_key=True, serialize=False)),
                ('brojradnihdana', models.IntegerField(blank=True, db_column='BrojRadnihDana', null=True)),
            ],
            options={
                'db_table': 'raspored',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rezervacija',
            fields=[
                ('idrez', models.IntegerField(db_column='IdRez', primary_key=True, serialize=False)),
                ('vreme', models.TimeField(db_column='Vreme')),
                ('ostvaren', models.IntegerField(blank=True, db_column='Ostvaren', null=True)),
                ('ocenazap', models.IntegerField(blank=True, db_column='OcenaZap', null=True)),
                ('ocenamusterija', models.IntegerField(blank=True, db_column='OcenaMusterija', null=True)),
            ],
            options={
                'db_table': 'rezervacija',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Slobodantermin',
            fields=[
                ('idst', models.AutoField(db_column='IdST', primary_key=True, serialize=False)),
                ('vreme', models.TimeField(db_column='Vreme')),
                ('slobodan', models.IntegerField(db_column='Slobodan')),
            ],
            options={
                'db_table': 'slobodantermin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tretman',
            fields=[
                ('idt', models.AutoField(db_column='IdT', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', max_length=45)),
                ('opis', models.CharField(blank=True, db_column='Opis', max_length=100, null=True)),
                ('cena', models.IntegerField(db_column='Cena')),
            ],
            options={
                'db_table': 'tretman',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zaposleni',
            fields=[
                ('idz', models.IntegerField(db_column='IdZ', primary_key=True, serialize=False)),
                ('imeprezime', models.CharField(db_column='ImePrezime', max_length=45)),
                ('zanimanje', models.CharField(db_column='Zanimanje', max_length=45)),
                ('bonus', models.IntegerField(blank=True, db_column='Bonus', null=True)),
                ('plata', models.IntegerField(db_column='Plata')),
                ('odobren', models.IntegerField(blank=True, db_column='Odobren', null=True)),
            ],
            options={
                'db_table': 'zaposleni',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KorisnikHasProizvod',
            fields=[
                ('korisnik', models.OneToOneField(db_column='Korisnik_Id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tasha.korisnik')),
            ],
            options={
                'db_table': 'korisnik_has_proizvod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Narucenproizvod',
            fields=[
                ('narudzbina_idnarudzbe', models.OneToOneField(db_column='Narudzbina_IdNarudzbe', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tasha.narudzbina')),
                ('kolicina', models.IntegerField()),
            ],
            options={
                'db_table': 'narucenproizvod',
                'managed': False,
            },
        ),
    ]
