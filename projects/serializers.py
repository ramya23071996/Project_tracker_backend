from rest_framework import serializers
from .models import MiniProject

class MiniProjectSerializer(serializers.ModelSerializer):
    assigned_to_username = serializers.ReadOnlyField(source='assigned_to.username')

    class Meta:
        model = MiniProject
        fields = '__all__'
