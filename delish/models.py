from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	
	def dish_count(self):
		return self.dish_set.count()
		
	def __unicode__(self):
		return self.name
		
class Chef(models.Model):
	name = models.CharField(max_length=100)
	
	def dish_count(self):
		return self.book_set.all()[0].dish_count()
		
	def __unicode__(self):
		return self.name
		
class Book(models.Model):
	name = models.CharField(max_length=100)
	chef = models.ForeignKey(Chef)
	link = models.CharField(max_length=200)
	
	def dish_count(self):
		return self.dish_set.count()
		
	def __unicode__(self):
		return self.name
		
class Dish(models.Model):
	name = models.CharField(max_length=100)
	ingredients = models.ManyToManyField(Ingredient)
	book = models.ForeignKey(Book)
	page = models.IntegerField()
	
	def __unicode__(self):
		return self.name
	
	
	
	
	
	