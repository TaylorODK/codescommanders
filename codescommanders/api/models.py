from django.db import models
from users.models import MyUser
# Create your models here.


class Order(models.Model):
    """Модель заказа."""
    name = models.CharField(
        max_length=128,
        blank=False
    )
    description = models.TextField(
        blank=True
    )
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        blank=False
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'user'),
                name='unique_order'
            )
        ]

    def __str__(self):
        return f"{self.name}"
