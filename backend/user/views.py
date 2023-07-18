from rest_framework import generics
from user.models import Customer
from user.serializers import CustomerSerializer, UserSerializer


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


class CustomerCreateView(generics.CreateAPIView):
    """Create a new customer."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a customer."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
