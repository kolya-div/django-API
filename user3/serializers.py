from rest_framework import serializers
from .models import ProfilakkModel

class ProfilakkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilakkModel
        fields = ('id', 'name', 'username', 'age', 'gender', 'birthday','bio')