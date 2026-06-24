from django.contrib import admin
from .models import User7Model

class User7Admin(admin.ModelAdmin):
    list_display = ('id', 'tadbir_nomi', 'tadbir_sanasi', 'joylashuv', 'maksimal_ishtirokchilar', 'chipta_narxi', 'user')

admin.site.register(User7Model, User7Admin)
