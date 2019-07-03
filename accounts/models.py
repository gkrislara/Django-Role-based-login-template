from django.contrib import auth
from django.db import models


class User(auth.models.AbstractUser):
    is_role1=models.BooleanField(default=False)
    is_role2=models.BooleanField(default=False)
    def __str__(self):
        return "@{}".format(self.username)
