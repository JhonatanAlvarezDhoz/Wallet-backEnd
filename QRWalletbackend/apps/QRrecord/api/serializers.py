from rest_framework import serializers
from apps.QRrecord.models import QRrecord, QRCategory


#---------------- QR  Serializers Category --------------
class QRCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = QRCategory
        fields = ('id', 'name', 'user_id',)

class CreateQRCategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = QRCategory
        fields = ('name', 'user_id',)

class UpdateQRCategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = QRCategory
        fields = ('name',)

class DeleteQRCategorySerilizers(serializers.ModelSerializer):
    
    class Meta:
        model = QRCategory
        fields = ('id',)


#---------------- QR  Serializers Category --------------
class QRrecordSerializers(serializers.ModelSerializer):

    class Meta: 
        model = QRrecord
        fields = ('name', 'value', 'qr_category', 'is_active',)

class CreateQRrecordSerializers(serializers.ModelSerializer):


    class Meta:
        model = QRrecord
        fields = ('name', 'value',)


class UpdateQRrecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = QRrecord
        fields = ('name', 'qr_category',)

class DeleteQRrecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = QRrecord
        fields = ('id',)

