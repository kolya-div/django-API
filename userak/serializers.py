from rest_framework import serializers
from .models import ProfilModel

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilModel
        fields = ('id', 'name', 'username', 'age', 'gender', 'birthday','bio')