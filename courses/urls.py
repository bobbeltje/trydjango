from django.urls import path
from .views import (
    CourseView,
    # my_fbv
    )

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    # path('', my_fbv, name='courses-list'),

    # path('', product_list_view, name='product-list'),
    # path('<int:id>/delete/', product_delete_view, name='product-delete'),
    # path('<int:id>', dynamic_lookup_view, name='product-detail'),
    # path('create/', product_create_view),
    # path('product/', product_detail_view),
]
