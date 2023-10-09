from django.contrib import admin

from .models import CerealCrops,LogShippedProducts,AuxiliaryMaterials

# Register your models here.
admin.site.register(CerealCrops)
admin.site.register(LogShippedProducts)
admin.site.register(AuxiliaryMaterials)

