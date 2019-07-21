from django.urls import path

from .views import (
    # article_list_view,
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView
    # article_detail_view,
    # dynamic_lookup_view
    )

# namespace
app_name = 'blogs'
urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    path('', ArticleListView.as_view(), name='article-list')
    # path('', article_list_view, name='article-list'),
    # path('<int:id>', dynamic_lookup_view, name='article-detail'),
    # path('blog/', article_detail_view)
]
