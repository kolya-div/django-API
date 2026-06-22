from django.db import models

class User7Model(models.Model):
    tadbir_nomi = models.CharField(max_length=200)
    tadbir_sanasi = models.DateTimeField()
    joylashuv = models.CharField(max_length=200)
    maksimal_ishtirokchilar = models.IntegerField()
    chipta_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.tadbir_nomi

    class Meta:
        db_table = "user7"