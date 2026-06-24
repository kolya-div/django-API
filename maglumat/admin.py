from django.contrib import admin
from .models import Magluma

# Register your models here.

class MaglumaAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', 'user')

admin.site.register(Magluma, MaglumaAdmin)