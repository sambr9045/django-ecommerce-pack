from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView, SignupView, ConfirmEmailView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("cart/", include("cart.urls")),
    path("accounts/", include("c_authentication.urls")),
    path("cpanel/", include("analitics.urls")),
    path("accounts/", include("allauth.urls")),
]
