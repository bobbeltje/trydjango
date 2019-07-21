from django.urls import path
from .views import (
    CourseListView,
    CourseView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    # my_fbv
    )

app_name = 'courses'
urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update')

]
