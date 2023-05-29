from django import template

register = template.Library()

@register.filter()
def language_code(url):
    return url.split("/")[1]