from django.contrib import admin
from .models import PaydaModel
# Register your models here.
class PaydaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age', 'birthday', 'bio')

admin.site.register(PaydaModel, PaydaAdmin)