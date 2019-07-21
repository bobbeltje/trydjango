from django.shortcuts import render
from django.views import View

# BASE VIEW Class = View

class CourseView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        return render(request, self.template_name, {})

# HTTP METHODS
# def my_fbv(request, *args, **kwargs):
#     return render(request, 'about.html', {})
