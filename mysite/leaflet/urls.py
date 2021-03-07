from django.urls import path
from . import views


urlpatterns = [
    #path('', TemplateView.as_view(template_name='maps/mapbox.html')),
    path('', views.leaflet_map, name='leaflet_map'),

]
