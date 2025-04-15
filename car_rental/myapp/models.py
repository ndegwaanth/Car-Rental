from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    id_no = models.IntegerField()
    phone_number = models.BigIntegerField()
    kra_pin = models.CharField()
    drivin_licence = models.CharField()
    date = models.DateTimeField(auto_created=True, auto_now=True, auto_now_add=False)
    email = models.EmailField(max_length=254)

