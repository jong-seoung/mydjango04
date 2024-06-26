from typing import Iterable
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class SuperUserManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_superuser=True)

class SuperUser(User):
    objects = SuperUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_superuser = True
        super().save(*args, **kwargs)