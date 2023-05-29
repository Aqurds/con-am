from django import template

from stories.models import StoryIndexPage

register = template.Library()

@register.simple_tag()
def simple_prayer():
    simple_prayer_details = StoryIndexPage.objects.first()
    simple_prayer_dict = {
        "simple_prayer_header": simple_prayer_details.simple_prayer_header,
        "simple_prayer": simple_prayer_details.simple_prayer,
    }
    
    return simple_prayer_dict


