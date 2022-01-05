from django.contrib import admin

from .models import computer
from .models import Basket
admin.site.register(computer)

admin.site.register(Basket)
# Register your models here.
