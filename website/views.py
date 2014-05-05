from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.
def index (request):
	t = get_template('index.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def learn (request):
	t = get_template('learn.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def browse (request, id_num):
	t = get_template('browse.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def ingredient (request, id_num):
	t = get_template('ingredient.html')
	html = t.render(Context({'id_num':id_num}))
	return HttpResponse(html)

def dish (request):
	t = get_template('dish.html')
	html = t.render(Context({'id_num':id_num}))
	return HttpResponse(html)

# def serve(request, path, document_root, show_indexes=False)
