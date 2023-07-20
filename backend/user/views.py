from rest_framework.permissions import IsAuthenticated
from rest_framework import (
    generics,
    permissions,
)
from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView
)
from user.serializers import (
    CustomerSerializer,
    UserSerializer
)
from user.models import Customer


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


class IsOwnerOnly(permissions.BasePermission):
    """Permission for Owner"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CustomerRetrieveUpdateView(RetrieveAPIView, UpdateAPIView):
    """Retrieve and update a customer."""
    permission_classes = [IsAuthenticated, IsOwnerOnly]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
