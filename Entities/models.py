from django.db import models
from phonenumber_field import modelfields
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager





# Client model, following the class diagramm specifications
class Client(models.Model):
    idClient = models.AutoField(primary_key=True, editable=False)
    emailClient = models.CharField(max_length=50)
    loginClient = models.CharField(max_length=20)
    passwordClient = models.CharField(max_length=24)
    adresseClient = models.CharField(max_length=50)
    telephoneClient = modelfields.PhoneNumberField()
    nomClient = models.CharField(max_length=50)
    prenomClient = models.CharField(max_length=50)
    dateDeCreationDuCompte = models.DateTimeField(auto_now_add=True)
    dateDeNaissanceClient = models.DateField(blank=True, null=True)
    avatarClient = models.ImageField(blank=True, null=True)
    descriptionClient = models.CharField(max_length=256, blank=True, null=True)


    def __str__(self) -> str:
        return self.loginClient




# Admin model, following the class diagramm specifications
class Administrateur(models.Model):
    idAdministrateur = models.AutoField(primary_key=True, editable=False)
    loginAdmin = models.CharField(max_length=20)
    passwordAdmin = models.CharField(max_length=24)
    
    def __str__(self):
        return self.loginAdmin


class AccountManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password):
        if not username :
            raise ValueError("Users must have a username")
        if not first_name :
            raise ValueError("Users must have a first name")
        if not last_name :
            raise ValueError("Users must have a last name")
        if not email :
            raise ValueError("Users must have an email")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )      

        user.set_password (password)
        user.save(using=self._db) 
        return user 

    def create_superuser(self, email, username, password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user








# Account model 
class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique=True)
    avatar = models.ImageField(null=True, blank=True)
    telephone = modelfields.PhoneNumberField(blank=True, null=True)
    cin = models.CharField(max_length=10, blank=True, null=True)


    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_login = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = AccountManager()


    def __str__(self) -> str:
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    




# Categorie model, following the class diagramm specifications

class Categorie(models.Model):
    idCategorie = models.AutoField(primary_key=True, editable=False)
    libelleCategorie = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleCategorie

    
    



# Article model, following the class diagramm specifications
class Article(models.Model):
    idArticle = models.AutoField(primary_key=True, editable=False)
    imageArticle = models.ImageField(blank=True, null=True)
    categorieArticle = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nomArticle = models.CharField(max_length=50)
    descriptionArticle = models.CharField(max_length=256)
    quantiteArticle = models.IntegerField()
    prixArticle = models.FloatField()
    dateAjoutArticle = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomArticle





# Mode de livraison model, following the class diagramm specifications
class ModeDeLivraison(models.Model):
    idModeDeLivraison = models.AutoField(primary_key=True, editable=False)
    libelleModeDeLivraison = models.CharField(max_length=50)
    descriptionModeDeLivraison = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleModeDeLivraison


# Mode de paiement model, following the class diagramm specifications
class ModeDePaiement(models.Model):
    idModeDePaiement = models.AutoField(primary_key=True, editable=False)
    libelleModeDePaiement = models.CharField(max_length=50)
    descriptionModeDePaiement = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleModeDePaiement


# Commande model, following the class diagramm specifications
class Commande(models.Model):
    idCommande = models.AutoField(primary_key=True, editable=False)
    modeDeLivraisonCommande = models.ForeignKey(ModeDeLivraison, on_delete=models.CASCADE)
    modeDePaiementCommande = models.ForeignKey(ModeDePaiement, on_delete=models.CASCADE)
    dateAjoutCommande = models.DateTimeField(auto_now_add=True)
    descriptionCommande = models.CharField(max_length=256)

    def __str__(self):
        return self.dateAjoutCommande



# Facture model, following the class diagramm specifications
class Facture(models.Model):
    idFacture = models.AutoField(primary_key=True, editable=False)
    clientFacture  = models.ForeignKey(Client, on_delete=models.CASCADE)
    datePaiementFacture = models.DateTimeField(auto_now_add=True)
    prixHtFacture = models.FloatField()
    totalHtFacture = models.FloatField()
    totalTtc = models.FloatField()

    def __str__(self):
        return "Facture de " + str(self.clientFacture)





    

