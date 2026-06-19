from django.contrib import admin
from .models import FoydalanuchilarModel
# Register your models here.
class FoydalanuchilarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'birthday', 'bio')

admin.site.register(FoydalanuchilarModel, FoydalanuchilarAdmin)