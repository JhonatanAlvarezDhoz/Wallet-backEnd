from django.urls import path
from apps.user.api.views import CreateUserAPIView, UserDetailsAPIView, TokenObtainPairAPIView, TokenRefreshAPIView, UpdateSubscribeAPIView

urlpatterns = [

    path('create/user/', CreateUserAPIView.as_view()),
    path('detail/user/', UserDetailsAPIView.as_view()),
    path('token/', TokenObtainPairAPIView.as_view()),
    path('token/refresh/', TokenRefreshAPIView.as_view()),
    path('subscribe/update/status/<pk>', UpdateSubscribeAPIView.as_view()),
]