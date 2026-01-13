from django.db import models


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AboutUs(DateTimeMixin):
    text = models.TextField()

    def __str__(self):
        return self.text
