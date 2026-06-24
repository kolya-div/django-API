from rest_framework.serializers import ModelSerializer
from .models import ProfilakkModel

class ProfilakkSerializer(ModelSerializer):
    class Meta:
        model = ProfilakkModel
        fields = ('id', 'name', 'username', 'age', 'gender', 'birthday','bio')

    def create(self, validated_data): 
        user = self.context['request'].user
        return ProfilakkModel.objects.create(user=user, **validated_data)