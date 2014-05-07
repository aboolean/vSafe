from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from tagging.models import TaggedItem
from django.views.decorators.csrf import csrf_exempt
from models import *
import itertools
import json

# Create your views here.
def index (request):
	t = get_template('index.html')
	html = t.render(Context({}))
	return HttpResponse(html)

def learn (request):
	t = get_template('learn.html')
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

@csrf_exempt
def subset (request):
	"""
	Includes all dishes if 'dishAll' True, else union of 'dishFilters' string. Same for ingredients.
	"""

	data = json.loads(request.body)

	REQUIRED_FIELDS = ['dishAll','ingredientAll','dishFilters','ingredientFilters']

	if sum([1 if e in data else 0 for e in REQUIRED_FIELDS]) != len(REQUIRED_FIELDS) or \
		request.method != 'POST':
		return HttpResponse(status=400)

	items = list()

	if data['dishAll'] == True:
		items.extend(list(Dish.objects.all()))
	else:
		items.extend(list(TaggedItem.objects.get_union_by_model(Dish, data['dishFilters'])))

	if data['ingredientAll'] == True:
		items.extend(list(Ingredient.objects.all()))
	else:
		items.extend(list(TaggedItem.objects.get_union_by_model(Ingredient, data['ingredientFilters'])))

	# identifier, name, image, vt, vg, classes, section
	response = []

	for item in items:
		# identifier
		if type(item) == Dish:
			identifier = 'D'
		elif type(item) == Ingredient:
			identifier = 'I'
		identifier += str(item.id)

		response.append({
			"identifier" : identifier,
			"name" : item.name,
			"image" : item.image,
			"vt" : item.isVegetarian,
			"vg" : item.isVegan,
			"classes" : [],
			})

	return HttpResponse(json.dumps(response), content_type="application/json", status=200)

@csrf_exempt
def list_all (request):
	"""
	Returns a mapping of all items and their identifiers.
	"""

	if request.method != 'GET':
		return HttpResponse(status=400)

	response = {}

	for dish in Dish.objects.all():
		response[dish.name] = 'D' + str(dish.id)

	for ingredient in Ingredient.objects.all():
		response[ingredient.name] = 'I' + str(ingredient.id)

	return HttpResponse(json.dumps(response), content_type="application/json", status=200)
