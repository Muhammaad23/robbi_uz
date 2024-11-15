from rest_framework import serializers
from .models import Mehmonhonlar

class MehmonhonlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mehmonhonlar
        fields = '__all__'  # Serialize all fields of the model
