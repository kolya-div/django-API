from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FoydalanuchilarModel(models.Model):
    name = models.CharField(max_length=90)
    username = models.CharField(max_length=77)
    age = models.IntegerField()
    birthday = models.DateField()
    bio = models.TextField(max_length=700)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "foydalanuvchilar"