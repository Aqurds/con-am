from django import template


register = template.Library()

@register.filter(name='directors_website')
def directors_website(word):
    return "View " + word + " Regional Website"
