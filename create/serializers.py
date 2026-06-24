from rest_framework.serializers import ModelSerializer
from .models import CreateModel

class CreateSerializer(ModelSerializer):
    class Meta:
        model = CreateModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')

    def create(self, validated_data):
        user = self.context['request'].user
        return CreateModel.objects.create(user=user, **validated_data)