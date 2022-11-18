from django.urls import path
from .views import *


urlpatterns = [
    path('', page_404, name='404'),
    path('sign-in/', sign_in, name='sign-in'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', for_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reset/', reset, name='reset'),
    path("staff/", staff_view, name="staff"),
    path("player/", player_view, name="player"),
    path("fc-andijan/", fc_view, name="fc"),
    path("club/", club_view, name="club"),
    path("stadium-image/<int:pk>/", stadium_image, name="stadium-image"),
    path("advertiser/", advertiser_view, name="advertiser"),
    path("news/", news_view, name="news"),
    path("video/", video_view, name="video"),
    path("info/", info_view, name="info"),
    path("about/", about_view, name="about"),
    path("region/", region_view, name="region"),
    path("preview/", preview_view, name="preview"),
    path("squad/", squad_view, name="squad"),
    path("line/", line_view, name="line"),
    path("subs/", subs_view, name="subs"),
    path("game/", game_view, name="game"),
    path("profile/<int:pk>/", profile_view, name="profile"),
    path("product/", product_view, name="product"),
    path("product-image/<int:pk>/", product_image, name="product-image"),
    path("get-stadium/<int:pk>/", get_stadium, name="get-stadium"),
    path("get-player/<int:pk>/", get_player, name="get-player"),
    path("get-staff/<int:pk>/", get_staff, name="get-staff"),
    path("add-staff/", add_staff, name="add-staff"),
    path("add-player/", add_player, name="add-player"),
    path("add-passes/", add_passes, name="add-passes"),
    path("add-stadium-image/", add_stadium_image, name="add-stadium-image"),
    path("add-stadium/", add_stadium, name="add-stadium"),
    path("add-fc/", add_fc, name="add-fc"),
    path("add-club/", add_club, name="add-club"),
    path("add-advertiser/", add_advertiser, name="add-advertiser"),
    path("add-video/", add_video, name="add-video"),
    path("add-news/", add_news, name="add-news"),
    path("add-info/", add_info, name="add-info"),
    path("add-about/", add_about, name="add-about"),
    path("add-preview/", add_preview, name="add-preview"),
    path("add-squad/", add_squad, name="add-squad"),
    path("add-line/", add_line, name="add-line"),
    path("add-subs/", add_subs, name="add-subs"),
    path("add-game/", add_game, name="add-game"),
    path("add-size/", add_size, name="add-size"),
    path("add-images/", add_images, name="add-images"),
    path("add-product/", add_product, name="add-product"),
    path("add-wishlist/", add_wishlist, name="add-wishlist"),
    path("add-region/", add_region, name="add-region"),
    path('delete-staff/<int:pk>/', delete_staff, name='delete-staff'),
    path('delete-player/<int:pk>/', delete_player, name='delete-player'),
    path('delete-passes/<int:pk>/', delete_passes, name='delete-passes'),
    path('delete-image/<int:pk>/', delete_image, name='delete-image'),
    path('delete-stadium/<int:pk>/', delete_stadium, name='delete-stadium'),
    path('delete-fc/<int:pk>/', delete_fc, name='delete-fc'),
    path('delete-club/<int:pk>/', delete_club, name='delete-club'),
    path('delete-advertiser/<int:pk>/', delete_advertiser, name='delete-advertiser'),
    path('delete-video/<int:pk>/', delete_videos, name='delete-video'),
    path('delete-news/<int:pk>/', delete_news, name='delete-news'),
    path('delete-info/<int:pk>/', delete_info, name='delete-info'),
    path('delete-about/<int:pk>/', delete_about, name='delete-about'),
    path('delete-preview/<int:pk>/', delete_preview, name='delete-preview'),
    path('delete-squad/<int:pk>/', delete_squad, name='delete-squad'),
    path('delete-line/<int:pk>/', delete_line, name='delete-line'),
    path('delete-subs/<int:pk>/', delete_subs, name='delete-subs'),
    path('delete-game/<int:pk>/', delete_game, name='delete-game'),
    path('delete-size/<int:pk>/', delete_size, name='delete-size'),
    path('delete-images/<int:pk>/', delete_product_image, name='delete-product-images'),
    path('delete-product/<int:pk>/', delete_product, name='delete-product'),
    path('delete-wishlist/<int:pk>/', delete_wishlist, name='delete-wishlist'),
    path('delete-region/<int:pk>/', delete_region, name='delete-region'),
    path('update-advertiser/<int:pk>/', update_advertiser, name='update-advertiser'),
    path('update-staff/<int:pk>/', update_staff, name='update-staff'),
    path('update-player/<int:pk>/', update_player, name='update-player'),
    path('update-passes/<int:pk>/', update_passes, name='update-passes'),
    path('update-stadium-image/<int:pk>/', update_stadium_image, name='update-stadium-image'),
    path('update-stadium/<int:pk>/', update_stadium, name='update-stadium'),
    path('update-fc/<int:pk>/', update_fc, name='update-fc'),
    path('update-club/<int:pk>/', update_club, name='update-club'),
    path('update-advertiser/<int:pk>/', update_advertiser, name='update-advertiser'),
    path('update-video/<int:pk>/', update_videos, name='update-video'),
    path('update-news/<int:pk>/', update_news, name='update-news'),
    path('update-info/<int:pk>/', update_info, name='update-info'),
    path('update-about/<int:pk>/', update_about, name='update-about'),
    path('update-preview/<int:pk>/', update_preview, name='update-preview'),
    path('update-squad/<int:pk>/', update_squad, name='update-squad'),
    path('update-line/<int:pk>/', update_line, name='update-line'),
    path('update-game/<int:pk>/', update_game, name='update-game'),
    path('update-size/<int:pk>/', update_size, name='update-size'),
    path('update-image/<int:pk>/', update_image, name='update-image'),
    path('update-product/<int:pk>/', update_product, name='update-product'),
    path('update-region/<int:pk>/', update_region, name='update-region'),
]
