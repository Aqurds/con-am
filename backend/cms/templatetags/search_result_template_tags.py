from django import template

from cms.models import HomePage

register = template.Library()

@register.simple_tag(takes_context=True)
def get_search_result_page_translatable_values(context):
    lang = context.get("current_language", None)
    return HomePage.objects.filter(locale__language_code=lang).first()