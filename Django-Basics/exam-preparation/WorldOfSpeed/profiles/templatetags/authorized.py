from django import template

from profiles.models import Profile

register = template.Library()


@register.simple_tag
def authorized():
    return Profile.objects.last()