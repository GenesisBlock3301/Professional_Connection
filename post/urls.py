from django.urls import path
from post.views import PostApiView
from company.views import CompanyAPIView

urlpatterns = [
    path("company/", CompanyAPIView.as_view()),
    path("posts/", PostApiView.as_view()),
    path("posts/<int:pk>/", PostApiView.as_view()),
]
