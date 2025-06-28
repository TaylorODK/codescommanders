from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from users.models import MyUser
from .models import Order
import datetime


class CustomUserSerializer(UserSerializer):
    """Кастомный сериализатор для отображения модели пользователя."""
    age = serializers.SerializerMethodField()

    class Meta:
        fields = UserSerializer.Meta.fields + ('age', 'date_birth')
        model = MyUser

    def get_age(self, obj):
        age = (datetime.date.today() - obj.date_birth).days//365
        return age


class CustomUserCreateSerializer(UserCreateSerializer):
    """Кастомный сериализатор для создания пользователя."""
    class Meta:
        fields = UserCreateSerializer.Meta.fields + ('date_birth',)
        model = MyUser

    def validate(self, data):
        if datetime.date.today() < data.get('date_birth'):
            raise serializers.ValidationError(
                'Нельзя выбрать дату рождения в будущем.'
            )
        return data


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели заказа."""
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'name',
            'description',
            'user',
        )

    def create(self, data):
        request = self.context.get('request')
        user = MyUser.objects.get(id=request.user.id)
        order = Order.objects.create(**data, user=user)
        return order
