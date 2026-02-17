from django.db import models

from core.models import DateTimeMixin


class TelegramUser(DateTimeMixin):
    telegram_id = models.PositiveBigIntegerField(unique=True)  # добавить unique

    def __str__(self):
        return str(self.telegram_id)