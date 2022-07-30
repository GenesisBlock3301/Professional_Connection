from django.contrib import admin
from django.urls import path, re_path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import swagger_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/accounts/", include("accounts.urls"), name="accounts")
]+swagger_urls.urlpatterns
