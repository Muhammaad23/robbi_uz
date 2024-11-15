from .models import Restoranlar
from rest_framework import serializers
from .models import Restoran_malumotlari
from .models import Menu

class RestoranlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restoranlar
        fields = ['id', 'title', 'jop_time', 'image', 'address', 'latitude', 'longitude']

    def create(self, validated_data):
        # Bu yerda yangi restoran obyektini yaratamiz
        return Restoranlar.objects.create(**validated_data)



class RestoranMalumotlariSerializer(serializers.ModelSerializer):
    # Optionally, you can add custom fields here if needed
    class Meta:
        model = Restoranlar
        fields = '__all__'

    # Custom method to handle creating an instance
    def create(self, validated_data):
        return Restoran_malumotlari.objects.create(**validated_data)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def create(self, validated_data):
        return Restoran_malumotlari.objects.create(**validated_data)