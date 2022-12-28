from rest_framework import serializers
from apps.QRrecord.models import QRrecord, QRCategory

class QRCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = QRCategory
        fields = ('name', 'user_id',)


class QRrecordSerializer(serializers.ModelSerializer):

    class Meta: 
        model = QRrecord
        fields = ('name', 'value', 'qr_category', 'is_active',)

