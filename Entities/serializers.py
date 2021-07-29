from rest_framework import serializers
from Entities.models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'idClient',
            'emailClient',
            'loginClient',
            'passwordClient',
            'adresseClient', 
            'telephoneClient',
            'nomClient', 
            'prenomClient',
            'dateDeNaissanceClient',
            'avatarClient',
            'descriptionClient',
        )

class  AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = (
            'idAdministrateur',
            'loginAdmin',
            'passwordAdmin',
        )

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = (
            'idCategorie',
            'libelleCategorie',
        )

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'idArticle',
            'categorieArticle',
            'nomArticle',
            'descriptionArticle',
            'quantiteArticle',
            'prixArticle',
            'dateAjoutArticle',
        )


class ModeDeLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeDeLivraison
        fields = (
            'idModeDeLivraison',
            'libelleModeDeLivraison',
            'descriptionModeDeLivraison',
        )


class ModeDePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeDePaiement
        fields = (
            'idModeDePaiement',
            'libelleModeDePaiement',
            'descriptionModeDePaiement',
        )

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = (
            'idCommande',
            'modeDeLivraisonCommande',
            'modeDePaiementCommande',
            'dateAjoutCommande',
            'descriptionCommande',
            
        )

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = (
            'idFacture',
            'datePaiementFacture',
            'prixHtFacture',
            'totalHtFacture', 
            'totalTtc',
            
        )