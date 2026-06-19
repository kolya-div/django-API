from django.contrib import admin
from .models import FoydaModel
# Register your models here.
class FoydaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'birthday', 'bio')

admin.site.register(FoydaModel, FoydaAdmin)