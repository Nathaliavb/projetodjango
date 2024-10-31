from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from requests import request
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View 
from django.views.generic import ListView, CreateView, DetailView, UpDateView


    
  
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
       cars = super().get_queryset().order_by('model')
       search = self.request.GET.get('search')
       if search:
        cars = cars.filter(model__icontains=search)
       return  cars
  
  
  
class NewCarView (View):
    
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
          new_car_form.save()
          return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
class NewCreateView(CreateView):
    model = Car
    form_class = CarModelForm 
    template_name = 'new_car.html'
    success_url = '/cars/'
    
    
class CarDetailView(DetailView):
    model = Car 
    template_name = 'car_detail.html'
    

class CarUpDateView(UpDateView):
    model = Car
    form_class = CarModelForm 
    template_name = 'car_update.html'
    success_url =  '/cars/'
    
     g