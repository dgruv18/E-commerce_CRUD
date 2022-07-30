from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied, NotAcceptable, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductDetailSerializer
from cart.models import Cart, CartItem
from cart.serializers import CartItemMiniSerializer


class CheckoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        total = (product.price * product.quantity)
        data = {}
        data["product"] = ProductDetailSerializer(
            product, context={"request": request}
        ).data
        data["total"] = total

        return Response(data, status=status.HTTP_200_OK)


class CheckoutCartView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        data = {}
        total = 0
        quantity = 0
        cart = get_object_or_404(Cart)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            total += item.product.price
            quantity += item.quantity
        end_total = (total * quantity)

        data["items"] = CartItemMiniSerializer(cart_items, many=True).data
        data["total"] = end_total
        return Response(data, status=status.HTTP_200_OK)