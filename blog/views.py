from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import ArticleForm

from .models import Article

class ArticleListView(ListView):
    # use template_name to overwrite location to look
    # template_name = 'blog/article_list.html'
    queryset = Article.objects.all()


# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'blog/article_list.html', context)

def article_detail_view(request):
    obj = Article.objects.get(id=1)
    context = {
    'object': obj
    }
    return render(request, 'blog/article_detail.html', context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        'object': obj
    }
    return render(request, 'blog/article_detail.html', context)
