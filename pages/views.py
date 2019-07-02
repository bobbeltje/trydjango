from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request)
	print(request.user)
	print(args, kwargs)
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, 'home.html', {})

def contact_view(*args, **kwargs):
	return HttpResponse('<h1>Contact page</h1>')
