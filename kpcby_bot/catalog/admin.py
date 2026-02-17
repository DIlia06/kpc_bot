from django.contrib import admin

from catalog.models import Printers, Mfu, OptionalEquipment, Consumables, Spares, RelatedProducts

admin.site.register(Printers)
admin.site.register(Mfu)
admin.site.register(OptionalEquipment)
admin.site.register(Consumables)
admin.site.register(Spares)
admin.site.register(RelatedProducts)