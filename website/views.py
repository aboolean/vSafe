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

	sub = [sub.dishes.all() for sub in ingredient_object.substitutee.all()]
	dishes = list(itertools.chain.from_iterable(sub))
	dishes = dishes + list(ingredient_object.dishes.all())
	dishes = sorted(list(set(dishes))) # remove duplices

	c = Context({'ingred':ingredient_object,'dishes':dishes})
	html = t.render(c)
	return HttpResponse(html)

def dish (request, id_num):
	t = get_template('dish.html')
	dish_object = Dish.objects.get(id=id_num)

	ingredients = dish_object.ingredients.all()
	substitutes = [list(ingred.substitutes.all()) for ingred in ingredients]
	substitutes = list(itertools.chain.from_iterable(substitutes))
	substitutes = sorted(list(set(substitutes)))

	c = Context({'dish':dish_object, 'subs':substitutes, 'ingredients':ingredients})
	html = t.render(c)
	return HttpResponse(html)

# def serve(request, path, document_root, show_indexes=False)
