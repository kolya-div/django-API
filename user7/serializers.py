from rest_framework.serializers import ModelSerializer
from .models import User7Model

class User7Serilizer(ModelSerializer):
    class Meta:
        model = User7Model
        fields = ('id', 'tadbir_nomi', 'tadbir_sanasi', 'joylashuv', 'maksimal_ishtirokchilar', 'chipta_narxi')
