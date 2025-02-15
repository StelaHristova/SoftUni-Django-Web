from Exam.utils import get_traveler_obj


class TravelerObjectMixin:

    def get_object(self, queryset=None):
        return get_traveler_obj()