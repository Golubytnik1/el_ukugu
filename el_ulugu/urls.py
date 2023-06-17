from django.contrib import admin
from django.urls import path, include
from el_ulugu.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation EL_UKUGU",
        default_version='v1',
        description="апи-документация проекта el_ukugu для фронтенд части;"
                    "присутствует для приложения chat, nalog, ugolovka.",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('', include('ugolovka.urls')),
    path('', include('nalog.urls')),
    path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
