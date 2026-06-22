from rest_framework.serializers import ModelSerializer
from .models import User5Model

class User5Serilizer(ModelSerializer):
    class Meta:
        model = User5Model
        fields = ('id', 'isbn_raqami', 'muallif_ismi', 'nashriyot_nomi', 'nashr_yili', 'sahifalar_soni')
