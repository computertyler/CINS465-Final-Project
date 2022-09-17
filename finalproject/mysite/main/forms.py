from django import forms
from . import models

class addGame(forms.Form):
    game = forms.CharField(label='Game name' , max_length=100)
    manufacturer = forms.CharField(label='Game manufacturer' , max_length=100)
    releaseYear = forms.IntegerField(label='year of release')
    def save(self):
        m_instance = models.Machine()
        m_instance.game = self.cleaned_data["game"]
        m_instance.manufacturer = self.cleaned_data["manufacturer"]
        m_instance.releaseYear = self.cleaned_data["releaseYear"]
        m_instance.save()
        return m_instance

class addLocation(forms.Form):
    address = forms.CharField(label='address' , max_length=100)
    state = forms.CharField(label='State' , max_length=100)
    zip = forms.IntegerField(label='zip code')
    machines = forms.ModelMultipleChoiceField(
        label='game',
        queryset=models.Machine.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )
    def save(self):
        l_instance = models.Location()
        l_instance.zip = self.cleaned_data["zip"]
        l_instance.state = self.cleaned_data["state"]
        l_instance.address = self.cleaned_data["address"]
        l_instance.save()
        l_instance.machines.add(self.cleaned_data["machines"].first())
        l_instance.save()
        return l_instance

    