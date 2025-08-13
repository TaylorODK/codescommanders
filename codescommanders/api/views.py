from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer
from .permissions import AuthorPermission

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = (AuthorPermission,)
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    lookup_field = "slug"
