from django import template

from stories.models import StoryIndexPage

register = template.Library()

@register.simple_tag()
def giving_initiative_details():
    giving_initiative_details = StoryIndexPage.objects.first()
    giving_initiative_details_dict = {
        "giving_initiative_header": giving_initiative_details.giving_initiative_header,
        "giving_initiative_content": giving_initiative_details.giving_initiative_content,
        "giving_initiative_button_text": giving_initiative_details.giving_initiative_button_text,
    }
    
    return giving_initiative_details_dict


