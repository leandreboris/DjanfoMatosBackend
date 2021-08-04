from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage




"""                             REST APIs for required entities                      """


# Client API
@csrf_exempt
def clientApi(request, id=0):

    if request.method == 'GET':
        if id != 0 :
            client = Client.objects.get(idClient=id)
            client_serializer = ClientSerializer(client)
            return JsonResponse(client_serializer.data, safe = False)
        client = Client.objects.all()
        client_serializer = ClientSerializer(client, many=True)
        return JsonResponse(client_serializer.data, safe = False)
    
    elif request.method=='POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        client_data = JSONParser().parse(request)
        client = Client.objects.get(idClient=client_data['idClient'])
        client_serializer = ClientSerializer(client, data=client_data)
        if client_serializer.is_valid() :
            client_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        client = Client.objects.get(idClient=id)
        client.delete()
        return JsonResponse("Deleted successfully", safe=False)



# Administrateur API
@csrf_exempt
def administrateurApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            administrateur = Administrateur.objects.get(idAdministrateur=id)
            administrateur_serializer = AdministrateurSerializer(administrateur)
            return JsonResponse(administrateur_serializer.data, safe = False)
        administrateur = Administrateur.objects.all()
        administrateur_serializer = AdministrateurSerializer(administrateur, many=True)
        return JsonResponse(administrateur_serializer.data, safe = False)
    
    elif request.method=='POST':
        administrateur_data = JSONParser().parse(request)
        administrateur_serializer = AdministrateurSerializer(data=administrateur_data)
        if administrateur_serializer.is_valid():
            administrateur_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        administrateur_data = JSONParser().parse(request)
        administrateur = Administrateur.objects.get(idAdministrateur=administrateur_data['idAdministrateur'])
        administrateur_serializer = AdministrateurSerializer(administrateur, data=administrateur_data)
        if administrateur_serializer.is_valid() :
            administrateur_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        administrateur = Administrateur.objects.get(idAdministrateur=id)
        administrateur.delete()
        return JsonResponse("Deleted successfully", safe=False)


# Categorie API
@csrf_exempt
def categorieApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            categorie = Categorie.objects.get(idCategorie=id)
            categorie_serializer = CategorieSerializer(categorie)
            return JsonResponse(categorie_serializer.data, safe = False)
        categorie = Categorie.objects.all()
        categorie_serializer = CategorieSerializer(categorie, many=True)
        return JsonResponse(categorie_serializer.data, safe = False)
    
    elif request.method=='POST':
        categorie_data = JSONParser().parse(request)
        categorie_serializer = CategorieSerializer(data=categorie_data)
        if categorie_serializer.is_valid():
            categorie_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        categorie_data = JSONParser().parse(request)
        categorie = Categorie.objects.get(idCategorie=categorie_data['idCategorie'])
        categorie_serializer = CategorieSerializer(categorie, data=categorie_data)
        if categorie_serializer.is_valid() :
            categorie_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        categorie = Categorie.objects.get(idCategorie=id)
        categorie.delete()
        return JsonResponse("Deleted successfully", safe=False)



# Article API
@csrf_exempt
def articleApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            article = Article.objects.get(idArticle=id)
            article_serializer = ArticleSerializer(article)
            return JsonResponse(article_serializer.data, safe = False)
        article = Article.objects.all()
        article_serializer = ArticleSerializer(article, many=True)
        return JsonResponse(article_serializer.data, safe = False)
    
    elif request.method=='POST':
        article_data = JSONParser().parse(request)
        article_serializer = ArticleSerializer(data=article_data)
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        article_data = JSONParser().parse(request)
        article = Article.objects.get(idArticle=article_data['idArticle'])
        article_serializer = ArticleSerializer(article, data=article_data)
        if article_serializer.is_valid() :
            article_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        article = Article.objects.get(idArticle=id)
        article.delete()
        return JsonResponse("Deleted successfully", safe=False)



# Mode de livraison API
@csrf_exempt
def modedelivraisonApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            modedelivraison = ModeDeLivraison.objects.get(idModeDeLivraison=id)
            modedelivraison_serializer = ModeDeLivraisonSerializer(modedelivraison)
            return JsonResponse(modedelivraison_serializer.data, safe = False)
        modedelivraison = ModeDeLivraison.objects.all()
        modedelivraison_serializer = ModeDeLivraisonSerializer(modedelivraison, many=True)
        return JsonResponse(modedelivraison_serializer.data, safe = False)
    
    elif request.method=='POST':
        modedelivraison_data = JSONParser().parse(request)
        modedelivraison_serializer = ModeDeLivraisonSerializer(data=modedelivraison_data)
        if modedelivraison_serializer.is_valid():
            modedelivraison_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        modedelivraison_data = JSONParser().parse(request)
        modedelivraison = ModeDeLivraison.objects.get(idModeDeLivraison=modedelivraison_data['idModeDeLivraison'])
        modedelivraison_serializer = ModeDeLivraisonSerializer(modedelivraison, data=modedelivraison_data)
        if modedelivraison_serializer.is_valid() :
            modedelivraison_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        modedelivraison = ModeDeLivraison.objects.get(idModeDeLivraison=id)
        modedelivraison.delete()
        return JsonResponse("Deleted successfully", safe=False)


# Mode de paiement API
@csrf_exempt
def modedepaiementApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            modedepaiement = ModeDePaiement.objects.get(idModeDePaiement=id)
            modedepaiement_serializer = ModeDePaiementSerializer(modedepaiement)
            return JsonResponse(modedepaiement_serializer.data, safe = False)
        modedepaiement = ModeDePaiement.objects.all()
        modedepaiement_serializer = ModeDePaiementSerializer(modedepaiement, many=True)
        return JsonResponse(modedepaiement_serializer.data, safe = False)
    
    elif request.method=='POST':
        modedepaiement_data = JSONParser().parse(request)
        modedepaiement_serializer = ModeDePaiementSerializer(data=modedepaiement_data)
        if modedepaiement_serializer.is_valid():
            modedepaiement_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        modedepaiement_data = JSONParser().parse(request)
        modedepaiement = ModeDePaiement.objects.get(idModeDePaiement=modedepaiement_data['idModeDePaiement'])
        modedepaiement_serializer = ModeDePaiementSerializer(modedepaiement, data=modedepaiement_data)
        if modedepaiement_serializer.is_valid() :
            modedepaiement_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        modedepaiement = ModeDePaiement.objects.get(idModeDePaiement=id)
        modedepaiement.delete()
        return JsonResponse("Deleted successfully", safe=False)

# Facture API
@csrf_exempt
def factureApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            facture = Facture.objects.get(idFacture=id)
            facture_serializer = FactureSerializer(facture)
            return JsonResponse(facture_serializer.data, safe = False)
        facture = Facture.objects.all()
        facture_serializer = FactureSerializer(facture, many=True)
        return JsonResponse(facture_serializer.data, safe = False)
    
    elif request.method=='POST':
        facture_data = JSONParser().parse(request)
        facture_serializer = FactureSerializer(data=facture_data)
        if facture_serializer.is_valid():
            facture_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        facture_data = JSONParser().parse(request)
        facture = Facture.objects.get(idFacture=facture_data['idFacture'])
        facture_serializer = FactureSerializer(facture, data=facture_data)
        if facture_serializer.is_valid() :
            facture_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        facture = Facture.objects.get(idFacture=id)
        facture.delete()
        return JsonResponse("Deleted successfully", safe=False)



# Commande API
@csrf_exempt
def commandeApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            commande = Commande.objects.get(idCommande=id)
            commande_serializer = CommandeSerializer(commande)
            return JsonResponse(commande_serializer.data, safe = False)
        commande = Commande.objects.all()
        commande_serializer = CommandeSerializer(commande, many=True)
        return JsonResponse(commande_serializer.data, safe = False)
    
    elif request.method=='POST':
        commande_data = JSONParser().parse(request)
        commande_serializer = CommandeSerializer(data=commande_data)
        if commande_serializer.is_valid():
            commande_serializer.save()
            return JsonResponse("Created successfully!!" , safe=False)
        return JsonResponse("Failed to create.",safe=False)

    elif request.method=='PUT':
        commande_data = JSONParser().parse(request)
        commande = Commande.objects.get(idCommande=commande_data['idCommande'])
        commande_serializer = CommandeSerializer(commande, data=commande_data)
        if commande_serializer.is_valid() :
            commande_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        commande = Commande.objects.get(idCommande=id)
        commande.delete()
        return JsonResponse("Deleted successfully", safe=False)


