from django.urls import path
from accounts.views.users import SignupView, UserProfileView, LogoutView, ProfileApiView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("user/", UserProfileView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
]+[
    path("profile/", ProfileApiView.as_view())
]
