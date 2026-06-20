from django.db import models

# Create your models here.
class ProfilakkModel(models.Model):
    name = models.CharField(max_length=90)
    username = models.CharField(max_length=77)
    age = models.IntegerField()
    birthday = models.DateField()
    g = (
        ('bala','Bala'),
        ('qiz','Qiz')
    )
    gender = models.CharField(max_length=90, choices=g)
    email = models.EmailField()
    def __str__(self):
        return self.username