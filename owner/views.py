from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import User
from owner.models import User 
from owner.models import Login
from owner.models import Trip
from datetime import datetime
from .models import Complaints
from django.contrib import messages
# from http.client import HTTPResponse

def index(request):
    return render(request, 'owner/index.html')

def register(request):
    return render(request, "templates/register.html",{})

def insertuser(request):
    if request.method=="POST":
        obj=User()
        obj.user_id = request.POST.get('user_id')
        obj.name = request.POST.get('name')
        obj.dob = request.POST.get('dob')
        obj.phone_number = request.POST.get('phone_number')
        obj.email = request.POST.get('email')
        obj.address = request.POST.get('address')
        obj.password = request.POST.get('password')
        obj.aadhar_number = request.POST.get('aadhar_number')
        obj.photo = request.FILES.get('photo')
        obj.aadhar_photo = request.FILES.get('aadhar_photo')
        obj.gender = request.POST.get('gender')
        obj.profession = request.POST.get('profession')
        obj.save()
        
        obb=Login()
        obb.user_name=obj.user_id
        obb.password=obj.password
        obb.type="user"
        obb.uid=obj.id
        obb.save()
        
        
    return render(request, 'owner/register.html')
   

def login(request):
    if request.method == "POST":
        unm = request.POST.get("username")
        passw = request.POST.get("password")
        obj = Login.objects.filter(user_name=unm,password=passw)
        # print(len(obj))
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.uid
            if tp == "admin":
                request.session["uid"]=uid
                return HttpResponseRedirect('/index/')
            elif tp == "user":
                request.session["uid"]=uid
                return HttpResponseRedirect('/index/')
            
        objlist = "email or password incorrect.....please try again....!"
        context = {
            'msg':objlist,
        }
        return render(request,'owner/login.html',context)

    return render(request,'owner/login.html')

def insert_trip(request):
    if request.method == "POST":
        obt = Trip()
        obt.user_id = "1"
        obt.start_location = request.POST.get('tripStart')
        obt.end_location = request.POST.get('tripEnd')
        obt.trip_date = request.POST.get('tripDate')
        trip_date = request.POST.get('tripDate')
        trip_time = request.POST.get('tripTime')
        datetime_str = f"{trip_date} {trip_time}"
        obt.trip_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        obt.vehicle_type = request.POST.get('vehicleType')
        obt.number_companion = request.POST.get('companions')
        obt.reason = request.POST.get('tripReason')
        obt.companion = request.POST.get('preferredCompanion')
        obt.save()  

    return render(request, 'owner/tripplan.html')





from django.shortcuts import render
from datetime import datetime
from .models import Trip

def search_trips(request):
    obk=""
    # Fetch all trips initially to display if no search is performed
    trips = Trip.objects.all()
    
    context = {
        'trips': trips,
        
    }

    if request.method == "POST":
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        trip_date = request.POST.get('trip_date')
        preferred_companion = request.POST.get('preferred_companion')

        # Start filtering based on the form input
        trips = trips.filter(
            start_location__icontains=from_location,
            end_location__icontains=to_location,
        )

        # If a trip date is provided, filter by date
        if trip_date:
            try:
                trip_date_obj = datetime.strptime(trip_date, '%Y-%m-%d')
                trips = trips.filter(trip_date__date=trip_date_obj)
            except ValueError:
                context['error'] = "Invalid date format. Please use YYYY-MM-DD."
                return render(request, 'owner/findride.html', context)

        # Filter based on gender preference, if selected
        if preferred_companion and preferred_companion != 'random':
            trips = trips.filter(companion__iexact=preferred_companion)

        if not trips.exists():
            context['message'] = "No trips found matching your criteria."

    # Update context with the filtered trips
    context['trips'] = trips

    return render(request, 'owner/findride.html', context)






# def submit_complaint(request):
#     if request.method == 'POST':
#         # Get form data from POST request
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Create a new complaint object and save it to the database
#         complaint = Complaints(
#             user_name=name,
#             email=email,
#             subject=subject,
#             messege=message  # Make sure "messege" matches your model's field
#         )
#         complaint.save()

#         # Show a success message using Django messages framework
#         messages.success(request, "Your message has been sent. Thank you!")

#         # Redirect to the same page or any other page after form submission
#         return redirect('submit_complaint')

#     # Render the page for GET requests
#     return render(request, 'owner/complaints.html')

def submit_complaint(request):
    if request.method=="POST":
        obj=Complaints()
        obj.user_name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.subject=request.POST.get('subject')
        obj.messege=request.POST.get('message')
        obj.save()
        messages.success(request, "Your message has been sent. Thank you!")
        return redirect('submit_complaint')
    return render(request, 'owner/complaints.html')
    