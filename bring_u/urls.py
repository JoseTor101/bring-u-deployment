from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from food_system import views as food_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food_system.urls')),
    path('accounts/', include('accounts.urls')),
    path('chat/', include('chat.urls')),
    path('', include('notifications.urls')),
    path('addmenu/', include('ai_ocr.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)