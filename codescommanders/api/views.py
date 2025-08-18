from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer
from .permissions import AuthorPermission
from .schemas import order_content_schema, product_content_schema, product_create_schema, order_create_schema
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = (AuthorPermission,)
    serializer_class = OrderSerializer

    @extend_schema(
        request=order_create_schema,
        responses=OrderSerializer,
        description="Создание нового заказа",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses=order_content_schema,
        description="Получение данных о заказе",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

@product_content_schema
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    lookup_field = "slug"
