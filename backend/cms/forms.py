from django import forms

from cms.models import ContactUsModel

from home.utils import send_email_template

from django.conf import settings


# class ContactUsSendEmailForm(forms.ModelForm):
#     class Meta:
#         model = ContactUsModel
#         fields = (
#             "contact_us_first_name",
#             "contact_us_last_name",
#             "contact_us_email",
#             "contact_us_phone_number",
#             "contact_us_church_name",
#             "contact_us_comment_and_message",
#         )

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop("request")
#         super().__init__(*args, **kwargs)

#     def save(self, *args, **kwargs):
#         contact_us = super().save(*args, **kwargs)
#         if self.request:
#             send_email_template(
#                 self.request.is_secure,
#                 "Get in touch",
#                 "cms/contact_us_email_template.html",
#                 [settings.DEFAULT_FROM_EMAIL],
#                 {
#                     "contact_us": contact_us,
#                 },
#             )
#         return contact_us
