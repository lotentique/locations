from django.shortcuts import render
import datetime
from django.utils import timezone
#from django.http import HttpResponse
from .models import Marques,Voitures,Clients,Locations,RetourVoiture,Penalisation
from .forms import MarqueForm,VoitureForm
# Create your views here.
def index(request):
    context={'message':"bonjour"} 
    return render(request,'voitures/base.html')

def voitures(request):
    marqueform=MarqueForm()
    voitureform=VoitureForm()
    lesmarques=Marques.objects.all()
    lesvoitures=Voitures.objects.filter(etat='0')
    #pour les requetes post
    if request.method=='POST':
        ajt=request.POST.get('ajt')
        ajtmodel=request.POST.get('ajtmodel')
        #l'ajout des models
        if ajtmodel :
            modele=request.POST.get('modele')
            nombre=request.POST.get('nombre')
            coutparjour=request.POST.get('coutparjour')
            marque=request.POST.get('marque')
            modeles=Marques.objects.filter(model=modele)
            marques=Marques.objects.filter(marque=marque)
            if (not modeles.exists()):
                nmarque=Marques.objects.create(
                    model=modele,
                    coutparjour=coutparjour,
                    marque=marque
                )
                message='marque et modele ajouter'
                type_message='success'
            else:
                message='se modele existe deja'
                type_message='info'
        #l'ajout des voitures
        else:
            matricule=request.POST.get('matricule')
            modele=request.POST.get('modele')
            marque=Marques.objects.get(model=modele)
            etat=request.POST.get('etat')
            voiture=Voitures.objects.filter(matricule=matricule)
            if not voiture.exists():
                Voitures.objects.create(
                    model=marque,
                    matricule=matricule,
                    etat=etat
                )
                message=' voiture ajouter'
                type_message='success'
            else:
                message=' voiture existe deja'
                type_message='info'
        context={'message':message,
            'marqueform':marqueform,
            'lesmarques':lesmarques,
            'lesvoitures':lesvoitures,
            'type_message':type_message,
            'voitureform':voitureform
        }
    #pour la methode get
    else:
        marqueform=MarqueForm()
        context={'marqueform':marqueform,
            'lesmarques':lesmarques,
            'lesvoitures':lesvoitures,
            'voitureform':voitureform
        }
    return render(request,'voitures/voitures.html',context)

def locations(request):
    nniaffichage=True
    
    if request.method=='POST':
        validernni=request.POST.get('validernni')
        valider=request.POST.get('valider')
        louer=request.POST.get('louer')
        #pour le formulaire de nni
        if validernni :
            lesmarques=Marques.objects.all()
            nni=request.POST.get('nni')
            nniclient=Clients.objects.filter(nni=nni)
            nniaffichage=False
            if  nniclient.exists():
                donneclient=False
            else :
                donneclient=True
            context={
                'message':nniaffichage,
                'donneclient':donneclient,
                'lesmarques':lesmarques,
                'nni':nni,
                'mod':True
            }
        #pour la deuxiene form nom-pre-model
        if valider:
            modele=request.POST.get('modele')
            lesvoitures=Voitures.objects.filter(model=modele,etat="0")
            nni=request.POST.get('nni')
            nom=request.POST.get('nom')
            prenom=request.POST.get('prenom')
            telephone=request.POST.get('telephone')
            voiture=True
            
            context={
                'nni':nni,
                'nom':nom,
                'prenom':prenom,
                'telephone':telephone,
                'lesvoitures':lesvoitures,
                'voiture':voiture,
                'modele':modele
            }
        #pour effectue la location
        if louer :
            nni=request.POST.get("nni")
            nom=request.POST.get("nom")
            prenom=request.POST.get("prenom")
            telephone=request.POST.get("telephone")
            matricule=request.POST.get("matricule")
            nbrjour=request.POST.get("nbrjour")
            modele=request.POST.get("modele")
            nbrjour=int(nbrjour)
            lemodele=Marques.objects.filter(model=modele)
            for lemodel in lemodele:
                coutparjour=lemodel.coutparjour
            montant=coutparjour*nbrjour
            date_fin=timezone.now()+datetime.timedelta(days=nbrjour)
            nniclient=Clients.objects.filter(nni=nni)
            objmatricule=Voitures.objects.get(matricule=matricule)
            if nniclient :
                client=Clients.objects.get(nni=nni)
            else:
                client=Clients.objects.create(
                    nni=nni,
                    nom=nom,
                    prenom=prenom,
                    telephone=telephone
                )
            nloca=Locations.objects.create(
                nni=client,
                matricule=objmatricule,
                date_fin=date_fin,
                montant=montant
            )
            Voitures.objects.filter(matricule=matricule).update(etat="1")
            context={
                'ten':"insertion avec sussce",
            }
    else:
        context={
            'message':nniaffichage
        }
    return render(request,'voitures/location.html',context)

def client(request):
    clients=Clients.objects.all()
    context={
        'clients':clients
    }
    return render(request,'voitures/client.html',context)
    