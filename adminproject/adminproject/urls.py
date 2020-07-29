from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', admin.site.urls),
    path('nlab/', include('app.urls'))
]



#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


