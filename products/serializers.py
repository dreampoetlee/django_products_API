from dataclasses import field
from rest_framework import serializers
from .models import Product

class CarsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ['title', 'description', 'price', 'inventory_quantity']