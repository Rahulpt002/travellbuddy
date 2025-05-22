from django.db import models


from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(unique=True, max_length=254)
    address = models.TextField()
    password = models.CharField(max_length=128)
    aadhar_number = models.CharField(unique=True, max_length=12)
    photo = models.CharField(max_length=100)
    aadhar_photo = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    profession = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'
        
        
        
        
class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    uid = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'login'

class Trip(models.Model):
    idtrip = models.AutoField(db_column='idTrip', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(max_length=45)
    start_location = models.CharField(max_length=45)
    end_location = models.CharField(max_length=45)
    trip_date = models.DateTimeField()
    trip_time = models.DateTimeField()
    vehicle_type = models.CharField(max_length=45)
    number_companion = models.IntegerField()
    reason = models.CharField(max_length=45)
    companion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'trip'


class Complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    messege = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'complaints'