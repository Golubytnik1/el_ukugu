from django.contrib import admin
from django.urls import path, include
from el_ulugu.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls'))
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
