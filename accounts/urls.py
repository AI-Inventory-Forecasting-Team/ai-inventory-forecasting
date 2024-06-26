from django.urls import path
from .views import (UserCreateView, UserDetailView, ProfileUpdateView, DeleteAccountView)


urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("profile/delete/", DeleteAccountView.as_view(), name="profile_delete"),
]