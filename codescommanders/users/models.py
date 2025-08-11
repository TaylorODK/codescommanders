from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """Класс модели пользователя."""

    email = models.EmailField(unique=True)
    date_birth = models.DateField(blank=False)
    REQUIRED_FIELDS = ["username", "date_birth"]
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=("username", "email"), name="unique_user"
            )
        ]

    def __str__(self):
        return f"{self.email}"
