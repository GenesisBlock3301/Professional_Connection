from django.urls import path
from . views import GroupPostApiView

urlpatterns = [
    path("gp_posts/", GroupPostApiView.as_view()),
    path("gp_posts/<int:pk>/", GroupPostApiView.as_view()),
]
