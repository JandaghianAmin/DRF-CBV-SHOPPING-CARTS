from rest_framework import serializers
from carts.models import carts, cartsItem
from products.models import Product


class simpleProductSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price']


class cartItemSerialzer(serializers.ModelSerializer):
    product = simpleProductSerilazer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cartitem:cartsItem):
        return cartitem.quntity * cartitem.product.price

    class Meta:
        model = cartsItem
        fields = ['id','product','quntity','total_price']

class cartSerializers(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    items = cartItemSerialzer(many=True,read_only=True)
    sum_all = serializers.SerializerMethodField()

    def get_sum_all(self, cart:carts):
    #    return  sum([item.quntity * item.product.price for item in cart.items.all()])
        return sum(obj.quntity * obj.product.price for obj in cart.items.all())
    class Meta:
        model = carts
        fields = ['id','items','sum_all']
