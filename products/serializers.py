from dataclasses import field
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [ 'id','image','title', 'description', 'price', 'inventory_quantity']