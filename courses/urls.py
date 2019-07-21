from django.urls import path
from .views import (
    CourseListView,
    CourseView,
    MyListView,
    # my_fbv
    )

app_name = 'courses'
urlpatterns = [
    path('', MyListView.as_view(), name='course-list'),
    # path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail')
    # path('', my_fbv, name='courses-list'),

]
