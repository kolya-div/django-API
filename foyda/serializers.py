from rest_framework import serializers
from .models import FoydaModel

class FoydaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoydaModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')