from django import template
from django.forms import BoundField

register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def add_tailwind_classes(value, arg):
    if not isinstance(value, BoundField):
        return value

    widget = value.field.widget
    css_classes = widget.attrs.get('class', '')
    css_class_list = css_classes.split()

    tailwind_classes = arg if arg else 'p-2 border rounded text-gray-600'

    if not set(tailwind_classes.split()).issubset(set(css_class_list)):
        widget.attrs['class'] = f"{css_classes} {tailwind_classes}".strip()

    return value
