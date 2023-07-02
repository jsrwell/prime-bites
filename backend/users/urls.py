from django.urls import path
from users.views import CreateUserView, CreateTokenView, MeView


app_name = 'users'

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', MeView.as_view(), name='me'),
]
