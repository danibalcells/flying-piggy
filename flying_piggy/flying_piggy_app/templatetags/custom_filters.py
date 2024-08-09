from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def div(value, arg):
    try:
        return Decimal(value) / Decimal(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def mul(value, arg):
    try:
        return Decimal(value) * Decimal(arg)
    except ValueError:
        return 0

@register.filter
def percentage(value, arg):
    try:
        return (Decimal(value) / Decimal(arg)) * 100
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def abs_value(value):
    return abs(value)