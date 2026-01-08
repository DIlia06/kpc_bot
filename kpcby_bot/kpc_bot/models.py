from django.db import models


class AboutUs(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class UserAppeal(models.Model):
    user_name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# class NameLinkMixin(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     link = models.CharField(max_length=255)
#
#     class Meta:
#         abstract = True

class Catalog(models.Model):
    printers = models.ForeignKey('Printers', on_delete=models.PROTECT)
    mfu = models.ForeignKey('Mfu', on_delete=models.PROTECT)
    optional_equipment = models.ForeignKey('OptionalEquipment', on_delete=models.PROTECT)
    consumables = models.ForeignKey('Consumables', on_delete=models.PROTECT)
    spares = models.ForeignKey('Spares', on_delete=models.PROTECT)
    related_products = models.ForeignKey('RelatedProducts', on_delete=models.PROTECT)

class Printers(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)

class Mfu(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)

class OptionalEquipment(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)

class Consumables(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)

class Spares(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)

class RelatedProducts(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255)
