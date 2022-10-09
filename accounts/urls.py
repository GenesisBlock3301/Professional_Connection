from django.urls import path
from accounts.views.users import SignupView, UserProfileView, LogoutView, ProfileApiView, send_friend_request,\
    accept_friend_request, delete_friend_request_0r_already_friend

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("user/", UserProfileView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
]+[
    path("profile/", ProfileApiView.as_view())
]+[
    path("send_friend_request/", send_friend_request)
]
