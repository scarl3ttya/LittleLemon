from django.shortcuts import render, HttpResponse
from django.core import serializers as djangoserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
import json
from datetime import datetime
from . import models, serializers, forms

# Function Views

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = models.Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def menu_item(request, pk=None): 
    if pk: 
        menu_item = models.Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = models.Booking.objects.all()
    booking_json = djangoserializer.serialize('json', bookings)
    return render(request, 'reservations.html',{"bookings":booking_json})

def book(request):
    form = forms.BookingForm()
    if request.method == 'POST':
        form = forms.BookingForm(request.POST)
        form = form.cleaned_data
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        
        reservation_exist = models.Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_time=data['reservation_time']).exists()
        
        if not reservation_exist:
            new_booking = models.Booking(
                reservation_name=data['reservation_name'],
                reservation_date=data['reservation_date'],
                reservation_time=data['reservation_time'],
                guest_count=data['guest_count'],
            )
            
            new_booking.save()
        else:
            return HttpResponse("{'message':'Reservation'}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = models.Booking.objects.all().filter(reservation_date=date)

    booking_json = djangoserializer.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')


# Class Views

class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [IsAuthenticated] 
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [IsAuthenticated] 


class BookingAPIViewset(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    #permission_classes = [IsAuthenticated] 
    
