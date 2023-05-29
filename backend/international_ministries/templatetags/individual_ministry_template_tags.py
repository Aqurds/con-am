from django import template


register = template.Library()


@register.simple_tag()
def get_first_word(word):
    return word.split(" ")[0]


@register.simple_tag()
def more_than_one_word_title(word):
    return len(word.split(" ", 1)) > 1


@register.simple_tag()
def get_other_words(word):
    return word.split(" ", 1)[1]

@register.filter()
def btn_give_to(word):
    return "Give to " + word

@register.filter()
def btn_website(word):
    return word + " website"