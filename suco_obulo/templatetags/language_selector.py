from django import template

register = template.Library()


@register.simple_tag
def language_selector():
    # Your logic for the language selector
    return "Language Selector Content"


@register.filter
def new_lang_code(current_lang_code):
    if current_lang_code == 'en':
        return 'tet'
    else:
        return 'en'


@register.filter
def new_lang_name(current_lang_code):
    if current_lang_code == 'en':
        return 'Tetum'
    else:
        return 'English'
