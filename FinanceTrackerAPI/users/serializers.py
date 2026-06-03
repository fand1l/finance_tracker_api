from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    model = CustomUser
    class Meta:
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']