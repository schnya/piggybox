from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('', include('piggybox.urls')),
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
