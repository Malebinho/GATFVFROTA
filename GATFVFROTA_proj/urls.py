from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GATFVFROTA_App.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
