from rest_framework.serializers import ModelSerializer
from .models import FoydalanuchilarModel

class FoydalanuchilarSerializer(ModelSerializer):
    class Meta:
        model = FoydalanuchilarModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')