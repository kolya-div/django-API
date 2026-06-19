from rest_framework import serializers
from .models import PaydaModel

class PaydaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaydaModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')