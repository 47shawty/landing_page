from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import contactView, successView

app_name = 'main'

urlpatterns = [
                  path('', views.HomeView.as_view(), name='home_url'),
                  path('contact/', contactView, name='contact_url'),
                  path('<slug:slug>/', views.ProductDetail.as_view(), name='productdetail_url'),
                  path('success/', successView, name='success_url'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
