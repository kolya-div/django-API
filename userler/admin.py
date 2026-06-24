from django.contrib import admin
from .models import AkkModel
# Register your models here.
class AkkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'birthday', 'bio',' user')

admin.site.register(AkkModel, AkkAdmin)