from django.db import models

from core.models import DateTimeMixin


class UserAppeal(DateTimeMixin):
    STATUS_CHOICES = (
        (1, 'Новое'),
        (2, 'В обработке'),
        (3, 'Закрыто'),
    )
    user = models.ForeignKey('users.TelegramUser', on_delete=models.PROTECT)
    theme = models.CharField(max_length=255)
    message = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
