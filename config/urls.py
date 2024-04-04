from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    # path('comments/', include('comments.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # jwt 토큰 발급
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # jwt 토큰 갱신
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # 스키마
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # 스웨거
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # 문서화
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)