from rest_framework.serializers import ModelSerializer
from .models import ProfilModel

class ProfilSerializer(ModelSerializer):
    class Meta:
        model = ProfilModel
        fields = ('id', 'name', 'username', 'age', 'gender', 'birthday','bio')

    def create(self,validated_data):
        user = self.context['request'].user
        return ProfilModel.objects.create(user=user, **validated_data)