from django.urls import path, include
from . import views
from allauth.account.views import LoginView, SignupView, ConfirmEmailView


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="authentication/login.html"),
        name="account_login",
    ),
    path(
        "signup/",
        SignupView.as_view(template_name="authentication/signup.html"),
        name="account_signup",
    ),
    path(
        "confirm-email/",
        ConfirmEmailView.as_view(template_name="account/email_verification_sent.html"),
        name="account_email_verification_sent",
    ),
    path(
        "confirm-email/(?P<key>[-:\w]+)/$",
        ConfirmEmailView.as_view(template_name="authentication/confirm-email.html"),
        name="account_confirm_email",
    ),
]
