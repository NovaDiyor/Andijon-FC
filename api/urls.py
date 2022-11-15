from django.urls import path
from .views import *


urlpatterns = [
    path("club/", Clubs),
    path("new/", New),
    path("single_new/<int:pk>/", Singlenews),
    path("academy/", Academy),
    path("game_view/", game_view),
    path("game_chart/", game_chart),
    path("media/", Media),
    path("single_media/<int:pk>/", Singlevideo),
    path("register/", Register),
    path("login/", login),
    path("shop/", Shop),
    path('singe_shop/<int:pk>/', Singleshop),
    path('wishlist_add/<int:pk>/', WishlistAdd),
    path('order_item_create/<int:pk>/', OrderItemCreate),
    path('order_create/', OrderCreate),
]
