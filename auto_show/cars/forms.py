from django import forms


class AddCarForm(forms.Form):
    title = forms.CharField(max_length=255)
    price = forms.IntegerField()
    description = forms.CharField(max_length=255)
