from django.db import models

# Create your models here.

class TestUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # This is not secure for real-world use
