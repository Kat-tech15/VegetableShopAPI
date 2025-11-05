from rest_framework import serializers
from .models import Vegetable

class VegetableSerializer(serializers.ModelSerializer):
    vendor_name = serializers.ReadOnlyField(source='vendor.username')

    class Meta:
        model = Vegetable
        fields = ['id', 'vendor', 'vendor_name', 'name', 'description', 'price_per_kg', 'available_quantity', 'image', 'date_posted']
        read_only_fields = ['vendor']

        