from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MyUser, Order
from .serializers import UserSerializer, OrderSerializer
from .permissions import AuthorPermission
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = (AuthorPermission,)
    serializer_class = OrderSerializer
