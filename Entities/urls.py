from django.conf.urls import url
from Entities import views




urlpatterns = [
    url(r'^clients$', views.clientApi),
    url(r'^clients/([0-9]+)$', views.clientApi),
    
    url(r'^clients/register$', views.ClientRegisterAPI.as_view(), name = 'Client Register API'),


    url(r'^administrateurs$', views.administrateurApi),
    url(r'^administrateurs/([0-9]+)$', views.administrateurApi),
    url(r'^administrateurs/register$', views.AdminRegisterAPI.as_view(), name = 'Admin Register API'),


    url(r'^categories$', views.categorieApi),
    url(r'^categories/([0-9]+)$', views.categorieApi),

    url(r'^articles$', views.articleApi),
    url(r'^articles/([0-9]+)$', views.articleApi),

    url(r'^livraisons$', views.modedelivraisonApi),
    url(r'^livraisons/([0-9]+)$', views.modedelivraisonApi),

    url(r'^paiements$', views.modedepaiementApi),
    url(r'^paiements/([0-9]+)$', views.modedepaiementApi),


    url(r'^factures$', views.factureApi),
    url(r'^factures/([0-9]+)$', views.factureApi),

    url(r'^commandes$', views.commandeApi),
    url(r'^commandes/([0-9]+)$', views.commandeApi),



]


