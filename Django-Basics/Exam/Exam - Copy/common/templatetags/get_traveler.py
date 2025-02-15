from django import template

from Exam.utils import get_traveler_obj
from travelers.models import Traveler

register = template.Library()


@register.simple_tag
def get_traveler():
    return get_traveler_obj()