from django.urls import path
from .views import SignupView, UserProfileView, LogoutView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("user/", UserProfileView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
]