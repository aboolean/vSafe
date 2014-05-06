from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from models import *
import itertools
# Create your views here.
def index (request):
	t = get_template('index.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def learn (request):
	t = get_template('learn.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def browse (request):
	t = get_template('browse.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def ingredient (request, id_num):
	t = get_template('ingredient.html')
	ingredient_object = Ingredient.objects.get(id=id_num)
	c = Context({'ingred':ingredient_object})
	html = t.render(c)
	return HttpResponse(html)

def dish (request, id_num):
	t = get_template('dish.html')
	dish_object = Dish.objects.get(id=id_num)
	substitutes = [ingred.substitutes.all() for ingred in dish_object.ingredients.all()]
	substitutes = list(itertools.chain.from_iterable(substitutes)).sort()
	substitutes = list(substitutes for substitutes,_ in itertools.groupby(substitutes))
	c = Context({'dish':dish_object, 'subs':substitutes})
	html = t.render(c)
	return HttpResponse(html)

# def serve(request, path, document_root, show_indexes=False)
