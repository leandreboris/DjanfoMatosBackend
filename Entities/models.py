from django.db import models
from phonenumber_field import modelfields




# Client model, following the class diagramm specifications
class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    emailClient = models.CharField(max_length=50)
    loginClient = models.CharField(max_length=20)
    passwordClient = models.CharField(max_length=24)
    adresseClient = models.CharField(max_length=50)
    telephoneClient = modelfields.PhoneNumberField()
    nomClient = models.CharField(max_length=50)
    prenomClient = models.CharField(max_length=50)
    dateDeNaissanceClient = models.DateField(blank=True, null=True)
    avatarClient = models.CharField(max_length=100, blank=True, null=True)
    descriptionClient = models.CharField(max_length=256, blank=True, null=True)



# Admin model, following the class diagramm specifications
class Administrateur(models.Model):
    idAdministrateur = models.AutoField(primary_key=True)
    loginAdmin = models.CharField(max_length=20)
    passwordAdmin = models.CharField(max_length=24)


# Categorie model, following the class diagramm specifications
class Categorie(models.Model):
    idCategorie = models.AutoField(primary_key=True)
    libelleCategorie = models.CharField(max_length=256)



# Article model, following the class diagramm specifications
class Article(models.Model):
    idArticle = models.AutoField(primary_key=True)
    categorieArticle = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nomArticle = models.CharField(max_length=50)
    descriptionArticle = models.CharField(max_length=256)
    quantiteArticle = models.IntegerField()
    prixArticle = models.FloatField()
    dateAjoutArticle = models.DateTimeField(auto_now_add=True)



# Mode de livraison model, following the class diagramm specifications
class ModeDeLivraison(models.Model):
    idModeDeLivraison = models.AutoField(primary_key=True)
    libelleModeDeLivraison = models.CharField(max_length=50)
    descriptionModeDeLivraison = models.CharField(max_length=256)

# Mode de paiement model, following the class diagramm specifications
class ModeDePaiement(models.Model):
    idModeDePaiement = models.AutoField(primary_key=True)
    libelleModeDePaiement = models.CharField(max_length=50)
    descriptionModeDePaiement = models.CharField(max_length=256)

# Commande model, following the class diagramm specifications
class Commande(models.Model):
    idCommande = models.AutoField(primary_key=True)
    modeDeLivraisonCommande = models.ForeignKey(ModeDeLivraison, on_delete=models.CASCADE)
    modeDePaiementCommande = models.ForeignKey(ModeDePaiement, on_delete=models.CASCADE)
    dateAjoutCommande = models.DateTimeField(auto_now_add=True)
    descriptionCommande = models.CharField(max_length=256)


# Facture model, following the class diagramm specifications
class Facture(models.Model):
    idFacture = models.AutoField(primary_key=True)
    datePaiementFacture = models.DateTimeField(auto_now_add=True)
    prixHtFacture = models.FloatField()
    totalHtFacture = models.FloatField()
    totalTtc = models.FloatField()




    

