from carts.models import carts,cartsItem
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework import generics
from . import serialzers

class cartsViewset(CreateModelMixin,
                   DestroyModelMixin,
                   RetrieveModelMixin,
                   GenericViewSet,):
    
    queryset = carts.objects.prefetch_related('items').all()
    serializer_class = serialzers.cartSerializers

class CartItemViewSet(ModelViewSet):
    serializer_class = serialzers.cartItemSerialzer

    def get_queryset(self):
        return cartsItem.objects.filter(carts_id=self.kwargs["carts_pk"]).select_related('product')
