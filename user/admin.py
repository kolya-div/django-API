from django.contrib import admin
from .models import UserModel
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'birthday', 'bio')

admin.site.register(UserModel, UserAdmin)