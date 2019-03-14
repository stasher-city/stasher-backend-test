import uuid
from hashlib import sha256

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def _default_id():
    return uuid.uuid4().hex


class CustomerManager(BaseUserManager):
    def get_by_natural_key(self, id_or_email):
        return self.filter(Q(email=id_or_email) | Q(id=id_or_email))


class Customer(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    id = models.TextField(
        primary_key=True,
        default=_default_id
    )

    email = models.EmailField(unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    gender = models.CharField(max_length=1)
    country_code = models.CharField(max_length=3)

    objects = BaseUserManager()

    def as_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'country_code': self.country_code
        }
