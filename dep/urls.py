from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView, SignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("cart/", include("cart.urls")),
    path("account/", include("c_authentication.urls")),
    path("cpanel/", include("analitics.urls")),
    path(
        "accounts/login/",
        LoginView.as_view(template_name="authentication/login.html"),
        name="account_login",
    ),
    path(
        "accounts/signup/",
        SignupView.as_view(template_name="authentication/signup.html"),
        name="account_signup",
    ),
    path("accounts/", include("allauth.urls")),
]
