from django.contrib import admin
from .models import User5Model

class User5Admin(admin.ModelAdmin):
    list_display = ('id', 'isbn_raqami', 'muallif_ismi', 'nashriyot_nomi', 'nashr_yili', 'sahifalar_soni')

admin.site.register(User5Model, User5Admin)
