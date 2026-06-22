from rest_framework.serializers import ModelSerializer
from .models import PaydaModel

class PaydaSerializer(ModelSerializer):
    class Meta:
        model = PaydaModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')