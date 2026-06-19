from django.db import models

# Create your models here.
class PaydaModel(models.Model):
    name = models.CharField(max_length=90)
    username = models.CharField(max_length=77)
    age = models.IntegerField()
    birthday = models.DateField()
    bio = models.TextField(max_length=700)
    def __str__(self):
        return self.name