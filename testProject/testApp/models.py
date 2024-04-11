from django.db import models

# Create your models here.
class TestModel(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class user_login(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
