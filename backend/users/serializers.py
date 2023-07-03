from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate, get_user_model


class PrimeUserSerializer(serializers.ModelSerializer):
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


class PrimeTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = 'Unable to authenticate with provided credentials.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
