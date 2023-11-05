from django.urls import path, include
from django.urls.converters import UUIDConverter
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('carts',views.cartsViewset,basename="carts")

carts_router = routers.NestedDefaultRouter(router,'carts',lookup="carts")
carts_router.register("items",views.CartItemViewSet,basename="item")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(carts_router.urls)),
 
]