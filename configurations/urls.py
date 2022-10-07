from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/accounts/", include("accounts.urls"), name="accounts"),
    path("api/v1/", include("company.urls"), name="company"),
    path("api/v1/", include("post.urls"), name="post"),
    path("api/v1/", include("group.urls"), name="group"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
