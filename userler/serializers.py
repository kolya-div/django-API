from rest_framework.serializers import ModelSerializer
from .models import AkkModel

class AkkSerializer(ModelSerializer):
    class Meta:
        model = AkkModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')

    def create(self, validated_data):
        user = self.context['request'].user
        return AkkModel.objects.create(user=user, **validated_data)