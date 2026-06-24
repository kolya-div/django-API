from rest_framework.serializers import ModelSerializer
from .models import UserModel

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'surname', 'age', 'birthday','bio')
    def create(self, validated_data):
        user = self.context['request'].user
        return UserModel.objects.create(user=user, **validated_data)    