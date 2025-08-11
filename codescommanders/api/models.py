from django.db import models
from users.models import MyUser

from codescommanders.constants import NAME_MAX_LENGTH

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        verbose_name="Наименование продукта",
        help_text=f"Максимальная длина наименования {NAME_MAX_LENGTH}",
    )
    slug = models.SlugField(
        max_length=NAME_MAX_LENGTH, blank=True, verbose_name="Слаг продукта"
    )
    description = models.TextField(
        blank=True, verbose_name="Описание продукта"
    )
    price = models.DecimalField(
        blank=False,
        verbose_name="Стоимость продукта",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Order(models.Model):
    """Модель заказа."""

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        verbose_name="Наименование заказа",
        help_text=f"Максимальная длина наименования {NAME_MAX_LENGTH}",
    )
    slug = models.SlugField(
        max_length=NAME_MAX_LENGTH, blank=True, verbose_name="Слаг заказа"
    )
    description = models.TextField(blank=True, verbose_name="Описание заказа")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=False)
    date_order = models.DateField(
        blank=False,
        verbose_name="Дата заказа",
        help_text="Укажите дату заказа в формате d.m.Y",
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        constraints = [
            models.UniqueConstraint(
                fields=("name", "user"), name="unique_order"
            )
        ]

    def __str__(self):
        return f"{self.name}"
