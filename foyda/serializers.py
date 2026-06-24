from rest_framework.serializers import ModelSerializer
from .models import FoydaModel

class FoydaSerializer(ModelSerializer):
    class Meta:
        model = FoydaModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')

    def create(self, validated_data):
        user = self.context['request'].user
        return FoydaModel.objects.create(user=user, **validated_data)