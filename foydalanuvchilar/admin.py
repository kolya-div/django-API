from django.contrib import admin
from .models import FoydalanuchilarModel
# Register your models here.
class FoydalanuchilarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'birthday', 'bio','user')

admin.site.register(FoydalanuchilarModel, FoydalanuchilarAdmin)