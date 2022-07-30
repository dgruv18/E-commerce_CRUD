from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import permissions, status, exceptions
from .serializers import (
    OrderItemSerializer,
    OrderItemMiniSerializer,
    OrderSerializer,
    OrderMiniSerializer,
)
from .models import Order, OrderItem
from .models import Product


class OrderView(APIView):

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        if product.quantity == 0:
            raise exceptions.NotAcceptable("quantity of this product is out.")
        try:
            order_number = request.data.get("order_number", "")
            quantity = request.data.get("quantity", 1)
        except:
            pass

        total = quantity * product.price
        order = Order().create_order(order_number, True)
        order_item = OrderItem().create_order_item(order, product, quantity, total)
        serializer = OrderItemMiniSerializer(order_item)
        self.time()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

