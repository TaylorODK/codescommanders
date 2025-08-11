from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from users.models import MyUser
from .models import Order, Product
import datetime


class CustomUserSerializer(UserSerializer):
    """Кастомный сериализатор для отображения модели пользователя."""

    age = serializers.SerializerMethodField()

    class Meta:
        fields = UserSerializer.Meta.fields + ("age", "date_birth")
        model = MyUser

    def get_age(self, obj):
        age = (datetime.date.today() - obj.date_birth).days // 365
        return age


class CustomUserCreateSerializer(UserCreateSerializer):
    """Кастомный сериализатор для создания пользователя."""

    class Meta:
        fields = UserCreateSerializer.Meta.fields + ("date_birth",)
        model = MyUser

    def validate(self, data):
        if datetime.date.today() < data.get("date_birth"):
            raise serializers.ValidationError(
                "Нельзя выбрать дату рождения в будущем."
            )
        return data


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели заказа."""

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Order
        fields = (
            "name",
            "slug",
            "description",
            "user",
            "date_order",
            "product"
        )

    def validate(self, data):
        date_order = data.get("date_order")
        if date_order and datetime.date.today() > date_order:
            raise serializers.ValidationError(
                "Нельзя выбрать дату заказа в прошлом."
            )
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        products = validated_data.pop("product", [])
        order = Order.objects.create(**validated_data, user=request.user)
        order.product.set(products)
        return order


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели продуктов."""
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "price",
            "description"
        )
