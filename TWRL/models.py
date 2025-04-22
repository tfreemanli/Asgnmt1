from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Room(BaseModel):
    title = models.CharField(max_length=255)
    room_number = models.IntegerField(unique=True, null=True)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Timeslot(BaseModel):
    orderby = models.IntegerField()
    title = models.CharField(max_length=255)

class Reservation(BaseModel):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator', null=True, blank=True)
    title = models.CharField(default="New Reservation", max_length=255) #reservation title for display
    desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class RSVDetail(BaseModel):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='rsv_details')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)