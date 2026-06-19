from rest_framework import serializers
from .models import CreateModel

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')