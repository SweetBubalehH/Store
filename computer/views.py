from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseNotModified
from .models import computer
from django.template import loader
from django.views import generic
from django.utils import timezone
import datetime as dt
from .models import computer
from .models import Basket
from cart.forms import CartAddProductForm

def hello(request):
    return HttpResponse("Тут будут компуктеры")

class ComputerView(generic.ListView):
    context_object_name = 'computer_list'
    model = computer
    template_name='computer/computer_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ComputerView, self).get_context_data(*args, **kwargs)

        now = 3
        context['expire'] = computer.objects.filter(tip=1)
       #context['new'] = User.objects.filter(joined_date__gt=now-d30)

        return context   
class PrinterView(generic.ListView):
    context_object_name = 'printer_list'
    model = computer
    template_name='computer/printer_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(PrinterView, self).get_context_data(*args, **kwargs)

        now = 3
        context['expire'] = computer.objects.filter(tip=2)
       #context['new'] = User.objects.filter(joined_date__gt=now-d30)

        return context            
    #template = loader.get_template('computer/computer_list.html')

#class EmployeeDetailView(generic.DetailView):
 #   context_object_name = 'comp'
  #  model = computer
   # template_name='computer/computer_detail.html'
    
def product_detail(request, id):
        product = get_object_or_404(computer,
                                id=id )
        cart_product_form = CartAddProductForm()
        return render(request, 'computer/computer_detail.html', {'product': product,
                                                  'cart_product_form': cart_product_form})    
    
class BasketView(generic.ListView):
    #context_object_name = 'computer_list'
    model = Basket
    template_name='computer/basket_list.html'
    #template = loader.get_template('computer/computer_list.html')

#def index(request):
   # computer_list = computer.objects.order_by('pub_date')
   # template = loader.get_template('computer/index.html')
  #  context = 
  #      {
  #      'computer_list': computer_list,
   #     }
  #  return HttpResponse(template.render(context, request))
# Create your views here.
