from rest_framework.serializers import ModelSerializer
from .models import User5Model

class User5Serilizer(ModelSerializer):
    class Meta:
        model = User5Model
        fields = ('id', 'isbn_raqami', 'muallif_ismi', 'nashriyot_nomi', 'nashr_yili', 'sahifalar_soni')

    def create(self, validated_data):
        user = self.context['request'].user
        return User5Model.objects.create(user=user, **validated_data)