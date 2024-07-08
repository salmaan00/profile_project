from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

    
@register.filter(name='add_attr')
def add_attr(field, attr_string):
    attr_name, attr_value = attr_string.split(':')
    return field.as_widget(attrs={attr_name: attr_value})