from django.db import models

from core.models import DateTimeMixin


class Catalog(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Printers(Catalog, DateTimeMixin):
    pass


class Mfu(Catalog, DateTimeMixin):
    pass


class OptionalEquipment(Catalog, DateTimeMixin):
    pass


class Consumables(Catalog, DateTimeMixin):
    pass


class Spares(Catalog, DateTimeMixin):
    pass


class RelatedProducts(Catalog, DateTimeMixin):
    pass
