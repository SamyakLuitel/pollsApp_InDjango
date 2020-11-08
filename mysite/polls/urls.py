from django.urls import path 
from . import views 


app_name = 'polls'

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /5/
    path('polls/<int:question_id>/', views.detail, name='detail'),
    # ex: /5/results/
    path('polls/<int:question_id>/results/', views.results, name='results'),
    # ex: /5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]


