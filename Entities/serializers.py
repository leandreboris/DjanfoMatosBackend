from rest_framework import serializers
from Entities.models import Client, Administrateur


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