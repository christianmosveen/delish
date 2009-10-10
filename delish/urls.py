from django.conf.urls.defaults import *

urlpatterns = patterns('codeandbeer.delish.views',
	(r'^$', 'index'),
	(r'^(?P<dish_id>\d+)/$', 'detail'),
	(r'^ingredient/(?P<ingredient_id>\d+)/$', 'ingredient_detail'),
)
