from django.db import models

# Create your models here.

class Marques(models.Model):
    model=models.CharField(max_length=30,primary_key=True)
    coutparjour=models.IntegerField()
    marque=models.CharField(max_length=30)

class Voitures(models.Model):
    ETAT=(('0','disponible'),('1','indisponible'))
    matricule=models.CharField(max_length=10,primary_key=True)
    model=models.ForeignKey(Marques,on_delete=models.CASCADE)
    etat=models.CharField(max_length=1,choices=ETAT)
    date_ajout=models.DateField(auto_now_add=True)

class Clients(models.Model):
    nni=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    telephone=models.IntegerField()

class Locations(models.Model):
    nlocation=models.AutoField(primary_key=True)
    nni=models.ForeignKey(Clients,on_delete=models.CASCADE)
    matricule=models.ForeignKey(Voitures,on_delete=models.CASCADE)
    date_location=models.DateTimeField(auto_now_add=True)
    date_fin=models.DateTimeField()
    montant=models.IntegerField()

class RetourVoiture(models.Model):
    nlocation=models.ForeignKey(Locations,on_delete=models.CASCADE)
    date_retour=models.DateTimeField()

class Penalisation(models.Model):
    nlocation=models.ForeignKey(RetourVoiture,on_delete=models.CASCADE)
    cout=models.IntegerField()
    raison=models.CharField(max_length=50)



