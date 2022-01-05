from django.urls import path
from . import views
app_name='catalog'

urlpatterns = [
    path('', views.catalog,name='cat'),
    # ex: /polls/5/
    #path('computer/<str:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
   # path('computer/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
   # path('computer/<int:question_id>/vote/', views.vote, name='vote'),
   
]