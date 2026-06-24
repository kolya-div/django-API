from rest_framework.serializers import ModelSerializer
from .models import Magluma

class MaglumaSerializer(ModelSerializer):
    class Meta:
        model = Magluma
        fields = ('title', 'content', 'created_at', 'updated_at')

    def create(self, validated_data):
        user = self.context['request'].user
        return Magluma.objects.create(user=user, **validated_data)