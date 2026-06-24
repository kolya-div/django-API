from django.contrib import admin
from .models import ProfilakkModel
# Register your models here.
class ProfilakkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'gender', 'birthday', 'email', 'user')

admin.site.register(ProfilakkModel, ProfilakkAdmin)