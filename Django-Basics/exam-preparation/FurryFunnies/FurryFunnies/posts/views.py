from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from FurryFunnies.utils import get_author_obj
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_author_obj()
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/details-post.html'
