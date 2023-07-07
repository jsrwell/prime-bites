from django.urls import path
from user.views import CreateUserView, AuthTokenView


app_name = 'user'

urlpatterns = [
    path('user/', CreateUserView.as_view(), name='create'),
    path('token/', AuthTokenView.as_view(), name='token'),
]
