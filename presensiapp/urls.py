from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('presensi/', include('presensi.urls')),
    path('admin/', admin.site.urls),
]
