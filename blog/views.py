from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import ArticleForm

from .models import Article

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    # method 1: overwrite the page to go to when saving form
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # method2: overwrite the page to go to when saving form
    def get_success_url(self):
        return '/'

class ArticleListView(ListView):
    # use template_name to overwrite location to look
    # template_name = 'blog/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    # use template_name to overwrite location to look
    # template_name = 'blog/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blogs:article-list')
