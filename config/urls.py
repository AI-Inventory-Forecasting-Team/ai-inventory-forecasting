from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base_index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('base_contact.html', TemplateView.as_view(template_name='base_contact.html'), name='contact'),
    path('base_about.html', TemplateView.as_view(template_name='base_about.html'), name='about'),
    path('base_pricing.html', TemplateView.as_view(template_name='base_pricing.html'), name='pricing'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)