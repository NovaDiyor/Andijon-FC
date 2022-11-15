from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_('Extra'), {'fields': ('status', 'country', 'number')}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(Staff)
admin.site.register(Players)
admin.site.register(Passes)
admin.site.register(Long)
admin.site.register(Helps)
admin.site.register(Kross)
admin.site.register(Squad)
admin.site.register(Line)
admin.site.register(Fc)
admin.site.register(Advertiser)
admin.site.register(News)
admin.site.register(Videos)
admin.site.register(Info)
admin.site.register(About)
admin.site.register(Game)
admin.site.register(Size)
admin.site.register(Substitute)
admin.site.register(Region)
admin.site.register(Images)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(OrderItem)
admin.site.register(Order)
