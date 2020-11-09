from django import template

register = template.Library()

@register.filter(name='division3')
def division3(number):
    return number if number % 3 == 0 else None
