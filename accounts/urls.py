from django.urls import path
from accounts.views.users_views import SignupView, UserProfileView, LogoutView, ProfileApiView
from accounts.views.connection_views import SendFriendRequest, AcceptFriendRequest, DeleteFriendRequestOrAlreadyFriend,\
    FriendList, BlockedFriendList

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("user/", UserProfileView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
]+[
    path("profile/", ProfileApiView.as_view())
]+[
    path("friend-list/", FriendList.as_view()),
    path("block-list/", BlockedFriendList.as_view()),
]+[
    path("send_friend_request/<user_id>/", SendFriendRequest.as_view()),
    path("accept_friend_request/<connection_id>/", AcceptFriendRequest.as_view()),
    path("delete_friend/<connection_id>/", DeleteFriendRequestOrAlreadyFriend.as_view())
]
