from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from users.serializers import PrimeUserSerializer, PrimeTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = PrimeUserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = PrimeTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class MeView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = PrimeUserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
