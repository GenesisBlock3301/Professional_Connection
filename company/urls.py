from django.urls import path
from company.views import CompanyAPIView

urlpatterns = [
    path("company/", CompanyAPIView.as_view()),
    path("company/<pk>/", CompanyAPIView.as_view()),
]
