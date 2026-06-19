from django.contrib import admin
from .models import ProfilModel
# Register your models here.
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'gender', 'birthday', 'bio')

admin.site.register(ProfilModel, ProfilAdmin)