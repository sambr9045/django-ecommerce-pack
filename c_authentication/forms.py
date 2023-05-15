from allauth.account.forms import LoginForm, SignupForm
from django import forms


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # added class form-control inf LoginForm Line 115

        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
        self.fields["remember"].widget.attrs.update({"class": "form-check-input"})


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove username if not needed for signup form
        self.fields.pop("username")

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "E-mail address"}
        )

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm password"}
        )

    # Add a new field for full name
    full_name = forms.CharField(
        max_length=50,
        label="Full Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Full Name"}
        ),
    )

    def save(self, request):
        # Get the default user object
        user = super(CustomSignupForm, self).save(request)

        # Save the full name to the user object
        user.full_name = self.cleaned_data["full_name"]
        user.save()

        return user
