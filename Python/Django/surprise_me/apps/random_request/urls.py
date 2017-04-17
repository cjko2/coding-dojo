from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^generate$', views.generate),
	url(r'^results$', views.results)
]