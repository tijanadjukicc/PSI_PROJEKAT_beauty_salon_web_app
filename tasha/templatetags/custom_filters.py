from django import template

register = template.Library()

@register.filter(name='get_val')
def get_val(a, key):
    # Your filter logic goes here
    return a.get(key)