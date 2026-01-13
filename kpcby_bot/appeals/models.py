from django.db import models

from core.models import DateTimeMixin


class UserAppeal(DateTimeMixin):
    user = models.ForeignKey('users.TelegramUser', on_delete=models.PROTECT)
    theme = models.CharField(max_length=255)
    message = models.TextField()
    status = models.IntegerField()
