from django.db import models

from core.models import DateTimeMixin


class NameLinkMixin(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Printers(NameLinkMixin, DateTimeMixin):
    pass


class Mfu(NameLinkMixin, DateTimeMixin):
    pass


class OptionalEquipment(NameLinkMixin, DateTimeMixin):
    pass


class Consumables(NameLinkMixin, DateTimeMixin):
    pass


class Spares(NameLinkMixin, DateTimeMixin):
    pass


class RelatedProducts(NameLinkMixin, DateTimeMixin):
    pass
