from django import forms

class MarqueForm(forms.Form):
    modele=forms.CharField(label='Modele',
        max_length=30,
        widget=forms.TextInput(attrs={'class':'form-controle'}),
        required=True
    )
    coutparjour=forms.IntegerField(label='Cout par jour',
        widget=forms.NumberInput(attrs={'class':'form-controle'}),
        required=True
    )
    marque=forms.CharField(label='Marque',
        max_length=30,
        widget=forms.TextInput(attrs={'class':'form-controle'}),
        required=True
    )

class VoitureForm(forms.Form):
    matricule=forms.CharField(label='matricule',
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-controle'}),
        required=True
    )