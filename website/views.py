from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from tagging.models import TaggedItem
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

def subset (request):
	"""
	Includes all dishes if 'dishAll' True, else union of 'dishFilters' string. Same for ingredients.
	"""
	REQUIRED_FIELDS = ['dishAll','ingredientAll','dishFilters','ingredientFilters']

	if sum([1 if e in request.DATA else 0 for e in REQUIRED_FIELDS]) != len(REQUIRED_FIELDS):
		return HttpResponse(status_code=400)

	items = list()

	if request.DATA['dishAll'] == True:
		items.extend(list(Dish.objects.all()))
	else:
		items.extend(list(TaggedItem.objects.get_union_by_model(Dish, request.DATA['dishFilters'])))

	if request.DATA['ingredientAll'] == True:
		items.extend(list(Ingredient.objects.all()))
	else:
		items.extend(list(TaggedItem.objects.get_union_by_model(Ingredient, request.DATA['ingredientFilters'])))

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

	return HttpResponse(json.dumps(response), content_type="application/json", status_code=200)
