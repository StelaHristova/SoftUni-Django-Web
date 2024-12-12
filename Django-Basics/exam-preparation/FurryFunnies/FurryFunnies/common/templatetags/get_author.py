from django import template

from FurryFunnies.utils import get_author_obj
from authors.models import Author

register = template.Library()


@register.simple_tag
def get_author():
    return get_author_obj()