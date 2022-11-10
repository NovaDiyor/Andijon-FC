from django.urls import path
from .views import *


urlpatterns = [
    path('', page_404, name='404'),
    path('sign-in/', sign_in, name='sign-in'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', for_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reset/', reset, name='reset'),
    path("about/", about_view, name="about"),
    path("add-about/", add_about, name="add-about"),
    path('delete-about/<int:pk>/', delete_about, name='delete-about'),
    path('update-about/<int:pk>/', update_about, name='update-about'),
]
