from django.urls import path

from .views import (
    article_list_view,
    article_detail_view,
    dynamic_lookup_view
    )

# namespace
app_name = 'blogs'
urlpatterns = [
    path('', article_list_view, name='article-list'),
    path('<int:id>', dynamic_lookup_view, name='article-detail'),
    path('blog/', article_detail_view)
]
