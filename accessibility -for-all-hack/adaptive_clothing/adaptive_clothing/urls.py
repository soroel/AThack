"""
URL configuration for adaptive_clothing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clothing_store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('clothing/', views.clothing_list, name='clothing_list'),
    path('clothing/<int:item_id>/order/', views.place_order, name='place_order'),
    path('order-confirmation/<int:item_id>/', views.order_confirmation, name='order_confirmation'),
    path('', views.homepage, name='homepage'),
    path('browse/', views.browse_clothing, name='browse_clothing'),
    path('sms-updates/', views.sms_updates, name='sms_updates'),
    path('mission/', views.mission, name='mission'),
    path('order-successful/<int:item_id>/', views.order_confirmation, name='order_confirmation'),
    #path('order-delivery/', views.order_delivery, name='order_delivery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
