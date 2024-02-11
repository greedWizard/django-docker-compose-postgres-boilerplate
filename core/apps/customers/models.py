from uuid import uuid4
from django.db import models

from core.apps.common.models import TimedBaseModel


class Customer(TimedBaseModel):
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=20,
        unique=True,
    )
    token = models.CharField(
        verbose_name='User Token',
        max_length=255,
        default=uuid4,
        unique=True,
    )

    def __str__(self) -> str:
        return self.phone

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
