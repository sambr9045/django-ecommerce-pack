from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


class CustomAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        print(template_prefix, email, context)
        # Build the email subject and body
        # subject = render_to_string('account/email/' + template_prefix + '_subject.txt', context)
        # subject = ''.join(subject.splitlines()) # Remove any newlines from subject
        # body_text = render_to_string('account/email/' + template_prefix + '.txt', context)
        # body_html = render_to_string('account/email/' + template_prefix + '.html', context)
        # text_content = strip_tags(body_text)

        # # Modify the email body to include custom message
        # body_text = f"Hello {context['user'].full_name},\n\n{body_text}"

        # # Create the email message
        # from_email = self.get_from_email()
        # msg = EmailMultiAlternatives(subject, body_text, from_email, [email])
        # msg.attach_alternative(body_html, "text/html")

        # Send the email message
        # msg.send()
        pass


class SendMail:
    def __init__(self, **kwargs):
        self.data = kwargs["data"]["data"]
        self.email = kwargs["data"]["email"]
        self.subject = kwargs["data"]["subject"]
        self.template_name = kwargs["data"]["template_name"]
        self.content = render_to_string(self.template_name, {"data": self.data})
        self.send_from = f"shamsubr <{kwargs['data']['send_from']}>"
        self.send()

    def Imsend(self):
        text_tags = strip_tags(self.content)
        return text_tags

    def send(self):
        to = self.email
        email = EmailMultiAlternatives(
            self.subject, self.Imsend(), self.send_from, [to]
        )
        email.attach_alternative(self.content, "text/html")
        email.send()
