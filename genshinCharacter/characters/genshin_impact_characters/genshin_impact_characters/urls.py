from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('characters/', include('characters.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns+= staticfiles_urlpatterns()
