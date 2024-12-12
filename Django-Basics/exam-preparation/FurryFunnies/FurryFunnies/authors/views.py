from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.mixins import AuthorObjectMixin
from authors.models import Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

    # def get_success_url(self):
    #     return reverse_lazy('dashboard')


class AuthorEditView(AuthorObjectMixin, UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author-details')


class AuthorDeleteView(AuthorObjectMixin, DeleteView):
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index-page')


class AuthorDetailsView(AuthorObjectMixin, DetailView):
    model = Author
    template_name = 'authors/details-author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        last_updated_post_title = self.object.posts.order_by('-updated_at').first()
        context['last_updated_post_title'] = last_updated_post_title if last_updated_post_title else 'N/A'

        return context
