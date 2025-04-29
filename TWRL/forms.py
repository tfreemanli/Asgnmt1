from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from TWRL.models import Room, Reservation

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

    password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label='Confirmed Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    def clean(self):
        cleaned_data = super().clean()
        passwd1 = cleaned_data.get("password1")
        passwd2 = cleaned_data.get("password2")

        if passwd1 and passwd2 and passwd1!= passwd2:
            raise ValidationError("Passwords doesn't match.")

        return cleaned_data

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
        fields = ['title', 'client', 'room', 'check_in_datetime', 'check_out_datetime', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
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

class CreateUSRForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

    password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label='Confirmed Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    def clean(self):
        cleaned_data = super().clean()
        passwd1 = cleaned_data.get("password1")
        passwd2 = cleaned_data.get("password2")

        if passwd1 and passwd2 and passwd1!= passwd2:
            raise ValidationError("Passwords doesn't match.")

        return cleaned_data

class UpdateUSRForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

class UpdateUsrPwdForm(forms.ModelForm):

    password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label='Confirmed Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        passwd1 = cleaned_data.get("password1")
        passwd2 = cleaned_data.get("password2")

        if passwd1 and passwd2 and passwd1!= passwd2:
            raise ValidationError("Passwords doesn't match.")

        return cleaned_data

class MyBookingCreateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['title', 'room', 'check_in_datetime', 'check_out_datetime', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-select'}),
            'check_in_datetime': forms.DateTimeInput(attrs={'class': 'form-control ', 'type': 'datetime-local'}),
            'check_out_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class MyBookingCreateStep2Form(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['title', 'desc', 'room', 'check_in_datetime', 'check_out_datetime']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class':'form-select', 'readonly':'readonly', 'onfocus': "this.defaultIndex=this.selectedIndex;", 'onchange': "this.selectedIndex=this.defaultIndex;"}),
            'check_in_datetime': forms.DateTimeInput(attrs={'class': 'form-control ', 'type': 'datetime-local', 'readonly': 'readonly' }),
            'check_out_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'readonly': 'readonly' }),
        }

    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request', None)
        room_id = kwargs.pop('room_id', None)
        check_in = kwargs.pop('check_in', None)
        check_out = kwargs.pop('check_out', None)

        super().__init__(*args, **kwargs)

        if room_id:
            self.fields['room'].initial = room_id

        if check_in:
            self.fields['check_in_datetime'].initial = check_in

        if check_out:
            self.fields['check_out_datetime'].initial = check_out