from django.contrib import admin
from .models import CreateModel
# Register your models here.
class CreateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'birthday', 'bio','user')

admin.site.register(CreateModel, CreateAdmin)