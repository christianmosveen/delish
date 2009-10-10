from django.shortcuts import render_to_response, get_object_or_404
from codeandbeer.delish.models import Dish, Ingredient, Chef, Book
from random import randint

def index(request):
	numberOfDishes = Dish.objects.count()
	dish = None
	if numberOfDishes > 0:
		dish = Dish.objects.all()[randint(0, numberOfDishes-1)]
	ingredients = Ingredient.objects.all().order_by('name')
	chefs = Chef.objects.all().order_by('name')
	books = Book.objects.all().order_by('name')
	return render_to_response('delish/index.html', {'dish': dish, 'ingredients': ingredients, 'chefs': chefs, 'books': books})

def detail(request, dish_id):
	dish = get_object_or_404(Dish, pk = dish_id)
	return render_to_response('delish/dish.html')

def ingredient_detail(request, ingredient_id):
	ingredient = get_object_or_404(Ingredient, pk = ingredient_id)
	dishes = ingredient.dish_set.all().order_by('name')
	return render_to_response('delish/ingredient.html', {'ingredient': ingredient, 'dishes': dishes})