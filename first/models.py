from django.db import models

# Create your models here.
class rent_payee(models.Model):
    p_email=models.EmailField(max_length=254)
    p_name=models.CharField(max_length=100)
    p_country=models.CharField(max_length=100)
    def __str__(self):
        return self.p_email

class Rentyourhouse(models.Model) :
    fullname = models.CharField(max_length=100)
    From = models.CharField(max_length=10)
    To = models.CharField(max_length=10)
    adults = models.CharField(max_length=1)
    children = models.CharField(max_length=1)
    phonenumber = models.CharField(max_length=10)
    appointment = models.TimeField()
    def __str__(self):
        return self.fullname


    
