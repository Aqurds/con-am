from django import forms as django_forms

from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxInput
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import (
    UserEditForm,
    UserCreationForm as WagtailUserCreationCustomForm,
)

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class CustomUserEditForm(UserEditForm):
    prayer_email_notification = django_forms.BooleanField(
        required=False,
        label=_("Prayer Email Notifications"),
    )
    giving_initiatives_email_notification = django_forms.BooleanField(
        required=False,
        label=_("Give Email Notifications"),
    )
    stories_email_notification = django_forms.BooleanField(
        required=False,
        label=_("Stories Email Notifications"),
    )


class CustomUserCreationForm(WagtailUserCreationCustomForm):
    prayer_email_notification = django_forms.BooleanField(
        required=False,
        label=_("Prayer Email Notifications"),
    )
    giving_initiatives_email_notification = django_forms.BooleanField(
        required=False,
        label=_("Give Email Notifications"),
    )
    stories_email_notification = django_forms.BooleanField(
        required=False,
        label=_("Stories Email Notifications"),
    )
