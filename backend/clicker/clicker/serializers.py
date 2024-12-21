from rest_framework import serializers
from .models import ClickData

class ClickDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickData
        fields = ['user', 'clicks', 'username']