from rest_framework import serializers
from apps.opinion.models import Opinion, Category


#---------------  Serializers Category Opinion   ---------------

class ListCategoryOpinionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


#---------------  Serializers Opinion   ---------------
class OpinionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['id', 'title', 'body', 'is_active', 'opinion_category', 'user']

class CreateOpinionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['title', 'body', 'is_active', 'opinion_category', 'user']

class UpdateOpinionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['title', 'body']

class DeleteOpinionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ['id']




