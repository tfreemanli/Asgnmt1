from django import forms
from django.contrib.auth.models import User

from TWRL.models import Room, Reservation, RSVDetail


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'room_number', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'room_number': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
        }

class CreateRSVForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['title', 'client','creator', 'room', 'check_in_datetime', 'check_out_datetime', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
            'creator': forms.HiddenInput(),
            'room': forms.Select(attrs={'class': 'form-select'}),
            'check_in_datetime': forms.DateTimeInput(attrs={'class': 'form-control ', 'type': 'datetime-local'}),
            'check_out_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class UpdateRSVForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['title', 'client', 'check_in_datetime', 'check_out_datetime', 'room', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
            'room': forms.Select(attrs={'class': 'form-select'}),
            'check_in_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'check_out_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

# class CreateRSVDetailForm(forms.ModelForm):
#     class Meta:
#         model = RSVDetail
#         fields = ['reservation', 'room', 'date', 'timeslot']
#         widgets = {
#             'reservation': forms.Select(attrs={'class': 'form-select'}),
#             'room': forms.Select(attrs={'class': 'form-select'}),
#             'date': forms.DateField(required=True),
#             'timeslot': forms.Select(attrs={'class': 'form-select'}),
#         }
