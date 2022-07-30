from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductDetailSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = "modified"


class OrderMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = "modified"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = "modified"


class OrderItemMiniSerializer(serializers.ModelSerializer):
    order = OrderMiniSerializer(required=False, read_only=True)
    product = ProductDetailSerializer(required=False, read_only=True)

    class Meta:
        model = OrderItem
        exclude = "modified"