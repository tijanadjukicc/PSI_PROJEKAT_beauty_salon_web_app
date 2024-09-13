from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *

class MyAppTestCase(TestCase):

    def setUp(self):
        # Set up initial data for tests
        self.client = Client()
        self.user = User.objects.create_user(username='Janko123', password='Janko123')
        self.korisnik = Korisnik.objects.create(id=self.user.id, korisnickoime='Janka123', lozinka='Janka123', email='janko@google.com')
        self.proizvod = Proizvod.objects.create(idp=1, naziv='Milka', cena=100, opis='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.kategorija = Kategorija.objects.create(idkat=1, naziv='Parfem')
        self.zaposleni = Zaposleni.objects.create(idz=1, korisnik=self.korisnik, imeprezime='Pera', zanimanje='Frizer')
        self.tretman = Tretman.objects.create(idt=1, naziv='Manikir', opis='aaaaaaaaaaaaaaaaaaa', cena=100)
        self.popust = Popusti.objects.create(id_popusta=1, procenat=10, kod_popusta='SLT50')
        self.musterija = Musterija.objects.create(idm=1, korisnik=self.korisnik)
        self.narudzbina = Narudzbina.objects.create(idnarudzbe=1, musterija_idm=self.musterija, ukupnacena='100', status=1, adresa='Radenka Ranovica 13', datum='2024-01-01', obradjena=0)
        self.ocena = Ocena.objects.create(ido=1, ocena=5, korisnik=self.korisnik)
        self.rezervacija = Rezervacija.objects.create(idrez=1, zaposleni_idz=self.zaposleni, musterija_idm=self.musterija, tretman_idt=self.tretman, vreme='10:00:00', ostvaren=0, datum='2024-01-01', ocenazap=0, ocenamusterija=0)

    # def test_product_list_view(self):
    #     response = self.client.get(reverse('prikazProizvoda'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'proizvodi.html')
    #     self.assertContains(response, 'Test Product')
    #
    # def test_product_detail_view(self):
    #     response = self.client.get(reverse('product_detail', args=[self.proizvod.idp]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'product_detail.html')
    #     self.assertContains(response, 'Test Product')
    #
    # def test_user_login_view(self):
    #     response = self.client.post(reverse('login'), {'username': 'Ana123', 'password': 'ana1234'})
    #     self.assertEqual(response.status_code, 302)  # Redirects to index on successful login
    #     self.assertRedirects(response, reverse('index'))
    #
    #     response = self.client.post(reverse('login'), {'username': 'Ana1234', 'password': 'ana1234'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
    #     self.assertContains(response, 'Pogrešna lozinka')
    #
    # def test_register_view(self):
    #     response = self.client.post(reverse('registracija'), {'username': 'Pera', 'password': 'Peric', 'email': 'pera@gmail.com'})
    #     self.assertEqual(response.status_code, 302)  # Redirects to login on successful registration
    #     self.assertRedirects(response, reverse('login'))
    #     self.assertTrue(User.objects.filter(username='Pera').exists())
    #     self.assertTrue(Korisnik.objects.filter(korisnickoime='Peric').exists())
    #
    # def test_add_to_cart(self):
    #     self.client.login(username='Janko123', password='Janko123')
    #     response = self.client.post(reverse('add_to_cart', args=[self.proizvod.idp]))  # Replace with your actual view name and URL parameters
    #     self.assertEqual(response.status_code, 302)  # Redirects to korpa
    #     self.assertTrue(KorisnikImaProizvodZaKorpu.objects.filter(korisnik=self.korisnik, proizvod=self.proizvod).exists())
    #
    # def test_finalize_order(self):
    #     self.client.login(username='Janko123', password='Janko123')
    #     KorisnikImaProizvodZaKorpu.objects.create(korisnik=self.korisnik, proizvod=self.proizvod, broj_proizvoda=1, cena_ukupna=100)
    #     response = self.client.post(reverse('finalize_order'), {
    #         'adresa': '123 Main St',
    #         'postarina': 'Standardna- 200.00din',
    #         'discount_code': 'SLT50'
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Order Confirmation')  # Adjust according to your confirmation message
    #
    # def test_add_to_favorites(self):
    #     self.client.login(username='Janko123', password='Janko123')
    #     response = self.client.post(reverse('add_to_favorites', args=[self.proizvod.idp]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(KorisnikHasProizvod.objects.filter(korisnik=self.korisnik, proizvod_idp=self.proizvod).exists())
    #     self.assertRedirects(response, reverse('prikazProizvoda'))
    #
    # def test_remove_from_favorites(self):
    #     self.client.login(username='Janko123', password='Janko123')
    #     KorisnikHasProizvod.objects.create(korisnik=self.korisnik, proizvod_idp=self.proizvod)
    #     response = self.client.post(reverse('remove_from_favorites', args=[self.proizvod.idp]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(KorisnikHasProizvod.objects.filter(korisnik=self.korisnik, proizvod_idp=self.proizvod).exists())
    #     self.assertRedirects(response, reverse('omiljeno_view'))
    #
    # def test_logout_view(self):
    #     self.client.login(username='Janko123', password='Janko123')
    #     response = self.client.get(reverse('logout'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('login'))
    #
    def test_prikazZaposlenih_view(self):
        response = self.client.get(reverse('prikazZaposlenih'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'zaposleni.html')
        self.assertContains(response, 'Test Employee')

# python manage.py test myapp