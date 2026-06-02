from rest_framework import serializers
from .models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    class Meta:
        fields = ['id', 'user', 'name', 'type']
        read_only_fields = ['id']


class TransactionSerializer(serializers.ModelSerializer):
    model = Transaction
    class Meta:
        fields = ['id', 'amount', 'description', 'date', 'category']
        read_only_fields = ['id', 'user']

    def validate_category(self, value):
        user = self.context['request'].user

        if value.user != user:
            raise serializers.ValidationError("You can use only your own categories")
        
        return value