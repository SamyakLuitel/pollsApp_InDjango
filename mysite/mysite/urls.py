from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('hello/', include('hello.urls')),
    path('polls/', include('polls.urls')),
    path('autos/', include('autos.urls')),
    path('maps/', include('maps.urls')),
    path('leaflet/', include('leaflet.urls')),
    path('tasks/', include('tasks.urls')),
    path('cats/', include('cats.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
