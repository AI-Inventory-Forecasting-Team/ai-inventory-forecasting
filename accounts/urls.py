from django.urls import path
from .views import (UserCreateView, UserDetailView)


urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("profile/", UserDetailView.as_view(), name="profile"),
]