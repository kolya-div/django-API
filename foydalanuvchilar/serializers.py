from rest_framework.serializers import ModelSerializer
from .models import FoydalanuchilarModel

class FoydalanuchilarSerializer(ModelSerializer):
    class Meta:
        model = FoydalanuchilarModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')

    def create(self, validated_data):
        user = self.context['request'].user
        return FoydalanuchilarModel.objects.create(user=user, **validated_data)