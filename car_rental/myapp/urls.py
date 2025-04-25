from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),  # Handles root URL: http://127.0.0.1:8000/myapp/
    path("hello/", views.hello),
    path("register/", views.register, name='register'),
    path("homepage/", views.homepage, name='homepage'),
    path("index/", views.index, name="template-testing"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)