from django.urls import path
from user.views import CreateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'user'

urlpatterns = [
    path('user/',
         CreateUserView.as_view(),
         name='create'
         ),
    path('api/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'
         ),
    path('api/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
         ),
    path('api/token/verify/',
         TokenVerifyView.as_view(),
         name='token_verify'
         ),
]
