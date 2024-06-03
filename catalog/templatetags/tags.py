from django import template

register = template.Library()


@register.filter()
def img(data):
    if data:
        return f'/media/{data}'
    return '#'