from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        ("Пользователь", USER),
        ("Админ", ADMIN),
        ("Модератор", MODERATOR)
    )


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=60)
    location = models.ManyToManyField(Location)
