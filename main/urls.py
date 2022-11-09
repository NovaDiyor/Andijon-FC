from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', for_login, name='login'),
    path('reset/', reset, name='reset'),
]+static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
