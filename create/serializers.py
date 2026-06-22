from rest_framework.serializers import ModelSerializer
from .models import CreateModel

class CreateSerializer(ModelSerializer):
    class Meta:
        model = CreateModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')