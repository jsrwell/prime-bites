from rest_framework import serializers
from django.contrib.auth import get_user_model

from user.models import Customer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

    def validate_first_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "First name cannot contain numbers.")

        return value

    def validate_last_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "Last name cannot contain numbers.")

        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")

        return value

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for the customer object."""

    class Meta:
        model = Customer
        fields = ['cpf', 'phone']
