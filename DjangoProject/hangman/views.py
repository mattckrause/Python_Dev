from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def test(request):
	template = loader.get_template('hello.html')
	context = {
		'title':'Test Page',
		'heading':'Hello, World App',
		'message':'This is my attempt at creating a Hello World app using Django. Unbelieveably bad css included.'
	}
	return HttpResponse(template.render(context,request))
