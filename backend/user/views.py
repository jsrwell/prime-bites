from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user."""

    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Add prime-bites-message and remove password from response."""
        response = super().create(request, *args, **kwargs)
        response.data['prime_bites_message'] = \
            f'User {response.data["first_name"]} has been created!'
        response.data.pop('password', None)

        return response
