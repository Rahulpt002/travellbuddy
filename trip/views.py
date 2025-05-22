from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from owner.models import User 
from owner.models import Login
from owner.models import Trip
# Create your views here.
def insert_trip(request):
    if request.method == "POST":
        obt = Trip()
        obt.user_id = "1"
        obt.start_location = request.POST.get('tripStart')
        obt.end_location = request.POST.get('tripEnd')
        obt.trip_date = request.POST.get('tripDate')
        obt.trip_time = request.POST.get('tripTime')
        obt.vehicle_type = request.POST.get('vehicleType')
        obt.number_companion = request.POST.get('companions')
        obt.reason = request.POST.get('tripReason')
        obt.companion = request.POST.get('gender')
        obt.save()  
    return render(request, 'trip/tripplan.html')
