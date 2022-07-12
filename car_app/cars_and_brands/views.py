from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import NameForm

def brands(request):
    brands = Brand.objects.all()
   
    return render(request, 'cars_and_brands/brands.html',{'brands': brands})
    
def new_brand(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name_form = form.cleaned_data['new_brand']
            country_form = form.cleaned_data['country']
            new_brand = Brand(name = name_form, country = country_form)
            new_brand.save()
            
            return HttpResponseRedirect('/brands/')
    else:
        form = NameForm()
    return render(request, 'cars_and_brands/new_brand.html', {'form':form})

def brand_detail(request):
    pass
def brand_edit(request):
    pass
def cars(request):
    pass
def new_car(request):
    pass
def car_detail(request):
    pass
def car_edit(request):
    pass
