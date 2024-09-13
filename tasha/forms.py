from django import forms
from .models import *

# forma za filtriranje proizvoda na osnovu kategorije - TIJANA DJUKIC
NACINI_SORTIRANJA = [
    (1, 'opadajuce'),
    (2, 'rastuce')
]
class FilterProductsKategorijaForm(forms.Form):
    kategorije = forms.MultipleChoiceField(
        choices=[],  # ovde ce zapravo biti nazivi kategorija
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        kategorije = kwargs.pop('categories', None)
        super(FilterProductsKategorijaForm, self).__init__(*args, **kwargs)
        if kategorije:
            self.fields['kategorije'].choices = kategorije

    sortMetoda = forms.ChoiceField(
        label= 'Sortiranje proizvoda',
        choices=NACINI_SORTIRANJA,
        widget=forms.RadioSelect(),
        required=False
    )

#forma za pretragu prizvoda/zaposlenig - TIJANA DJUKIC
class SearchForm(forms.Form):
    searchField = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search . . .', 'required': True, 'class': 'form-control'}
        ),
        required=False
    )

#forma za isplatu plate zaposlenima - TIJANA DJUKIC
class DropboxZaposleni(forms.Form):
    def __init__(self, *args, **kwargs):
        zaposleni_choices = kwargs.pop('zaposleni_choices', None)
        super(DropboxZaposleni, self).__init__(*args, **kwargs)
        if zaposleni_choices:
            self.fields['zaposleni'] = forms.ChoiceField(choices=zaposleni_choices)

    zaposleni = forms.ChoiceField(
        choices=[],
        label=''
    )

#forma za zakazivanje termina - TIJANA DJUKIC
class zakazivanjeDan(forms.Form):
    tretmani = forms.ChoiceField(
        choices=[],
        label='Odaberite tretman:',
        required=True
    )

    zaposleniZak = forms.ChoiceField(
        choices=[],
        label='Odaberite zaposlenog:',
        widget=forms.RadioSelect(),
        required=True
    )

    # vreme = forms.ChoiceField(
    #     choices=[],
    #     label='',
    #     widget=forms.RadioSelect(),
    #     required=True
    # )

    datum = forms.DateField(
        label='Odaberite datum:',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        zaposleni_choices = kwargs.pop('zaposleni_choices', None)
        tretmani_choices = kwargs.pop('tretmani_choices', None)
        zanimanje = kwargs.pop('zanimanje', None)
        # vreme_choices = kwargs.pop('vreme_choices', None)
        super(zakazivanjeDan, self).__init__(*args, **kwargs)
        if zaposleni_choices:
            self.fields['zaposleniZak'].choices = zaposleni_choices
        if tretmani_choices:
            self.fields['tretmani'].choices = tretmani_choices
        if zanimanje:
            self.fields['zaposleni'].widget.attrs['class'] = zanimanje
        # if vreme_choices:
        #     self.fields['vreme'].choices = vreme_choices

# forma za zakazivanje termina - TIJANA DJUKIC
class formaTermini(forms.Form):
    termini = forms.ChoiceField(
        choices=[],
        label='',
        widget=forms.RadioSelect(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        termini_choices = kwargs.pop('termini_choices', None)
        # vreme_choices = kwargs.pop('vreme_choices', None)
        super(formaTermini, self).__init__(*args, **kwargs)
        if termini_choices:
            self.fields['termini'].choices = termini_choices

# forma potrebna za ocenjivanje zaposlenog - DJUNJA COLIC
class OcenaForm(forms.Form):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    ocena = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        label='Ocenite ocenom od 1 do 5'
    )