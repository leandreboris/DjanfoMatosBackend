from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Administrateur)
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(ModeDeLivraison)
admin.site.register(ModeDePaiement)
admin.site.register(Commande)
admin.site.register(Facture)
