from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    #path('', TemplateView.as_view(template_name='maps/mapbox.html')),
    path('', views.default_map, name='default_map'),

]
