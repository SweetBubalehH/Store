from django.urls import include, path
from . import views


app_name='computer'

urlpatterns = [
 
    path('cart/<int:product_id>', include('cart.urls')),
   path('', views.ComputerView.as_view(),name="computer_list"),
   path('printer/', views.PrinterView.as_view(),name="printer"),
   #path('create/', views.create,name='create'),
   path('basket/', views.BasketView.as_view(), name='basket'),
   path('<int:id>/', views.product_detail, name='computer-detail'),

   
   
]