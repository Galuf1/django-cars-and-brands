from django import forms

class NameForm(forms.Form):
    new_brand = forms.CharField(label='new_brand', max_length=100)
    country = forms.CharField(label='country',max_length=100)