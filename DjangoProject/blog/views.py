from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def blog(request):
	test = "hello, world!"
	template = loader.get_template('blog.html')
	context = {
		'title':'Matt\'s Blog',
		'heading':'Blog Title',
		'message':'Blah blah blah, this is my blog. Pretend I\'m writing something interesting here.'
	}
	return HttpResponse(template.render(context,request))