from rest_framework.serializers import ModelSerializer
from .models import PaydaModel

class PaydaSerializer(ModelSerializer):
    class Meta:
        model = PaydaModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')

    def create(self, validated_data): 
        user = self.context['request'].user
        return PaydaModel.objects.create(user=user, **validated_data)