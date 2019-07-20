from django.urls import path
from .views import (
    product_list_view,
    product_detail_view, 
    product_delete_view,
    product_create_view,
    product_list_view,
    render_initial_data,
    dynamic_lookup_view
    )

# namespace
app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('<int:id>', dynamic_lookup_view, name='product-detail'),
    path('create/', product_create_view),
    path('product/', product_detail_view),
]
