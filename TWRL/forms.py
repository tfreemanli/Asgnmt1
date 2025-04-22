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
        fields = ['title', 'client','creator', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
            'creator': forms.HiddenInput(),
        }

class UpdateRSVForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['title', 'client', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
        }

class CreateRSVDetailForm(forms.ModelForm):
    class Meta:
        model = RSVDetail
        fields = ['reservation', 'room', 'date', 'timeslot']
        widgets = {
            'reservation': forms.Select(attrs={'class': 'form-select'}),
            'room': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateField(required=True),
            'timeslot': forms.Select(attrs={'class': 'form-select'}),
        }
