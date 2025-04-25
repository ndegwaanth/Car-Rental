from __future__ import unicode_literals
from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    id_no = models.IntegerField()
    phone_number = models.BigIntegerField()
    kra_pin = models.CharField(max_length=50)
    drivin_licence = models.CharField(max_length=50)
    date = models.DateTimeField(auto_created=True, auto_now=True, auto_now_add=False)
    email = models.EmailField(max_length=254)
    file = models.FileField(upload_to='uploads/')

    class Meta:
        db_table = "client"
