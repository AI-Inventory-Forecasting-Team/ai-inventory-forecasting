from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='signup'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]