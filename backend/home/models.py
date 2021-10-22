from django.conf import settings
from django.db import models


class Car(models.Model):
    "Generated Model"
    num = models.BigIntegerField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="car_user",
    )
