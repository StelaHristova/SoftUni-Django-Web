class LabelAddMixin:
    image_label = ''

    def add_labels(self):
        for field_name, field in self.fields.items():
            if field_name == 'image_url':
                field.label = self.image_label
            else:
                label = field_name.replace('_', ' ').title()
                field.label = label

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_labels()


class ReadOnlyMixin:
    def make_fields_readonly(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()