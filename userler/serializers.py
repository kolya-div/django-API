from rest_framework import serializers
from .models import AkkModel

class AkkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AkkModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')