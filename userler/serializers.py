from rest_framework.serializers import ModelSerializer
from .models import AkkModel

class AkkSerializer(ModelSerializer):
    class Meta:
        model = AkkModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')