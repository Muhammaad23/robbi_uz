from rest_framework import serializers
from .models import Kilinika_sanatoriya

class KilinikaSanatoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kilinika_sanatoriya
        fields = '__all__'  # Include all fields from the model
