from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib import admin

app_name = 'tasks'
urlpatterns = [
    #path('', TemplateView.as_view(template_name='maps/mapbox.html')),
    path('', views.index, name='todo'),
    path('admin/', admin.site.urls),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),





]
