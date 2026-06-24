from django.db import models
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "user3"