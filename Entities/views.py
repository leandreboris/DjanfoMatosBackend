from Entities.models import Client, Administrateur
from Entities.serializers import ClientSerializer, AdministrateurSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http.response import JsonResponse




"""                             REST APIs for required entities                      """


# Client API
@csrf_exempt
def clientApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            client = Client.objects.get(clientId=id)
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
        client = Client.objects.get(clientId=client_data['clientId'])
        client_serializer = ClientSerializer(client, data=client_data)
        if client_serializer.is_valid() :
            client_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        client = Client.objects.get(clientId=id)
        client.delete()
        return JsonResponse("Deleted successfully", safe=False)



# Administrateur API
@csrf_exempt
def administrateurApi(request, id=0):

    if request.method == 'GET':
        if id != 0:
            administrateur = Administrateur.objects.get(administrateurId=id)
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
        administrateur = Administrateur.objects.get(administrateurId=administrateur_data['administrateurId'])
        administrateur_serializer = AdministrateurSerializer(administrateur, data=administrateur_data)
        if administrateur_serializer.is_valid() :
            administrateur_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE' :
        administrateur = Administrateur.objects.get(administrateurId=id)
        administrateur.delete()
        return JsonResponse("Deleted successfully", safe=False)