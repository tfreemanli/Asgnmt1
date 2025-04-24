from django.contrib.auth.models import User
from django.db import models

from django.core.exceptions import ValidationError

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

# class MyUser(User):
#     usr = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255, null=True, blank=True)
#     desc = models.CharField(max_length=255, null=True, blank=True)

class Timeslot(BaseModel):
    orderby = models.IntegerField()
    title = models.CharField(max_length=255)

class Reservation(BaseModel):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator', null=True, blank=True)
    title = models.CharField(default="New Reservation", max_length=255) #reservation title for display
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    check_in_datetime = models.DateTimeField()
    check_out_datetime = models.DateTimeField()
    desc = models.CharField(max_length=255, null=True, blank=True)

    def clean(self):
        if self.check_in_datetime >= self.check_out_datetime:
            raise ValidationError("Check-in date must be before check-out date.")

        overlapping_reservations = Reservation.objects.filter(
            room=self.room,
            check_in_datetime__lt=self.check_out_datetime,
            check_out_datetime__gt=self.check_in_datetime
        ).exclude(id=self.id)

        if overlapping_reservations.exists():
            raise ValidationError("Reservation already exists.")

    def __str__(self):
        return self.title

class RSVDetail(BaseModel):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='rsv_details')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)