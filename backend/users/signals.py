from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.http import HttpRequest

from users.models import User
from prayers.models import Prayer
from stories.models import StoryPage
from give.models import SpecialGivingPage
from cms.models import ContactUsForm

from home.utils import send_mass_mail


@receiver(post_save, sender="prayers.Prayer")
def send_email_notification_for_prayer(sender, instance: Prayer, **kwargs):
    """
    This function sends an email whenever a new Prayer, Giving Initiative, Story, Timely update and News is added
    """
    subscriber_group = Group.objects.get(name="Subscriber")
    prayer_subscribers = User.objects.filter(
        groups=subscriber_group, prayer_email_notification=True
    )
    request = HttpRequest()
    datatuple = [
        ("Prayer Notification", [subscriber.email], {})
        for subscriber in prayer_subscribers
    ]

    if prayer_subscribers:
        send_mass_mail(
            request,
            "prayers/prayer_email_template.html",
            datatuple,
        )


@receiver(post_save, sender="give.SpecialGivingPage")
def send_email_notification_for_giving_initiatives(
    sender, instance: SpecialGivingPage, **kwargs
):
    """
    This function sends an email whenever a new Prayer, Giving Initiative, Story, Timely update and News is added
    """
    subscriber_group = Group.objects.get(name="Subscriber")
    giving_initiatives_subscribers = User.objects.filter(
        groups=subscriber_group, giving_initiatives_email_notification=True
    )
    request = HttpRequest()
    datatuple = [
        ("Giving Initiatives Notification", [subscriber.email], {})
        for subscriber in giving_initiatives_subscribers
    ]

    if giving_initiatives_subscribers:
        send_mass_mail(
            request,
            "give/giving_initiative_email_template.html",
            datatuple,
        )


@receiver(post_save, sender="stories.StoryPage")
def send_email_notification_for_stories(sender, instance: StoryPage, **kwargs):
    subscriber_group = Group.objects.get(name="Subscriber")
    stories_subscribers = User.objects.filter(
        groups=subscriber_group, stories_email_notification=True
    )
    request = HttpRequest()
    datatuple = [
        ("Stories Notification", [subscriber.email], {})
        for subscriber in stories_subscribers
    ]

    if stories_subscribers:
        send_mass_mail(
            request,
            "stories/stories_email_template.html",
            datatuple,
        )
