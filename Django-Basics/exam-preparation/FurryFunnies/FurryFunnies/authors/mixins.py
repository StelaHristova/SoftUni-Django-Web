from FurryFunnies.utils import get_author_obj


class AuthorObjectMixin:

    def get_object(self, queryset=None):
        return get_author_obj()