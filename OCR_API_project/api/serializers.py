from .models import ImageUpload
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'
