from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    money = models.IntegerField(default=0)
    maximumMoney = models.IntegerField(default=0)
    heroStrength = models.IntegerField(default=1)
    heroSpeed = models.IntegerField(default=1)
    heroDurability = models.IntegerField(default=1)
    chosenLeague = models.IntegerField(default=1)