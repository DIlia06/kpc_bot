from django.db import models

from core.models import DateTimeMixin


class TelegramUser(DateTimeMixin):
    telegram_id = models.PositiveBigIntegerField()
