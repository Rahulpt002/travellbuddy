from django.db import models

# Create your models here.
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