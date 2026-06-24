from django.db import models
from django.contrib.auth.models import User

class User5Model(models.Model):
    isbn_raqami = models.CharField(max_length=20, unique=True)
    muallif_ismi = models.CharField(max_length=200)
    nashriyot_nomi = models.CharField(max_length=200)
    nashr_yili = models.IntegerField()
    sahifalar_soni = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.isbn_raqami

    class Meta:
        db_table = "user5"