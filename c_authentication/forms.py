from allauth.account.forms import LoginForm


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form fields
        # self.fields["email"].widget.attrs.update(
        #     {"class": "form-control", "placeholder": "Username"}
        # )

        # added class form-control inf LoginForm Line 115

        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
        self.fields["remember"].widget.attrs.update({"class": "form-check-input"})
