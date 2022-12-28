from rest_framework import serializers
from apps.user.models import User
from apps.QRrecord.models import QRCategory

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'is_subscribe', 'is_free',)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        QRCategory.objects.create(name='Food', user_id=user)
        QRCategory.objects.create(name='Ubication', user_id=user)

        return user

        

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username"
            "email",
            ""
            "subscribe_date",
            "first_name",
            "is_free",
        )