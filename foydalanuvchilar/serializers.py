from rest_framework import serializers
from .models import FoydalanuchilarModel

class FoydalanuchilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoydalanuchilarModel
        fields = ('id', 'name', 'username', 'age', 'birthday','bio')