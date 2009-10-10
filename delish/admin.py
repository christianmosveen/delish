from codeandbeer.delish.models import Dish
from codeandbeer.delish.models import Ingredient
from codeandbeer.delish.models import Chef
from codeandbeer.delish.models import Book
from django.contrib import admin

admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Chef)
admin.site.register(Book)