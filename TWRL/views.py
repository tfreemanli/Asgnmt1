from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from TWRL.forms import *
from TWRL.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

class Register(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edited_user'] = self.object
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        new_passwd = form.cleaned_data['password1']
        user.set_password(new_passwd)
        user.save()
        messages.add_message(self.request, messages.SUCCESS, "User registered successfully! Please login.")
        return super().form_valid(form)


class RoomList(ListView):
    model = Room
    template_name = 'rsv_step1.html'

################ Room management
class ManagementRoomList(ListView):
    model = Room
    ordering = 'room_number'
    template_name = 'management/roomlist.html'

class ManagementRoomCreate(CreateView):
    model = Room
    template_name = 'management/roomcreate.html'
    #fields = ['title', 'room_number', 'desc']
    success_url = reverse_lazy('management_room_list')
    form_class = CreateRoomForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ManagementRoomUpdate(UpdateView):
    model = Room
    template_name = 'management/roomdetail.html'
    form_class = CreateRoomForm
    success_url = reverse_lazy('management_room_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# class ManagementRoomBook(CreateView):
#     model = Reservation
#     template_name = 'management/rsvcreate.html'
#     fields = ['client', 'creator', 'title', 'desc']
#     success_url = reverse_lazy('management_rsvDetail_create')
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())


class ManagementRoomDelete(DeleteView):
    model = Room
    template_name = 'management/roomdelete.html'
    success_url = reverse_lazy('management_room_list')

#################### RSV management
class ManagementRSVList(ListView):
    model = Reservation
    template_name = 'management/rsvlist.html'

class ManagementRSVCreate(CreateView):
    model = Reservation
    template_name = 'management/rsvcreate.html'
    success_url = reverse_lazy('management_rsv_list')
    form_class = CreateRSVForm

    def form_valid(self, form):
        try:
            form.instance.creator = self.request.user
            self.object = form.save(commit=False)
            # self.object.user = self.request.user
            self.object.full_clean()
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        except ValidationError as e:
            #messages.error(self.request, e.message)
            form.add_error(None, e)
            return self.form_invalid(form)

class ManagementRSVUpdate(UpdateView):
    model = Reservation
    template_name = 'management/rsvdetail.html'
    form_class = UpdateRSVForm
    # success_url = request.path
    success_url = reverse_lazy('management_rsv_list')

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            # self.object.user = self.request.user
            # messages.success(self.request, "Updated successfully!")
            self.object.full_clean()
            self.object.save()
            # return HttpResponseRedirect(self.request.path)
            return HttpResponseRedirect(self.get_success_url())
        except ValidationError as e:
            # messages.error(self.request, e.message)
            form.add_error(None, e)
            return self.form_invalid(form)

class ManagementRSVDelete(DeleteView):
    model = Reservation
    template_name = 'management/rsvdelete.html'
    success_url = reverse_lazy('management_rsv_list')

############# User management

class ManagementUSRList(ListView):
    model = User
    template_name = 'management/usr_list.html'

class ManagementUSRCreate(CreateView):
    model = User
    template_name = 'management/usr_create.html'
    success_url = reverse_lazy('management_usr_list')
    form_class = CreateUSRForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edited_user'] = self.object
        context['user'] = self.request.user
        return context

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        user = form.save(commit=False)
        new_passwd = form.cleaned_data['password1']
        user.set_password(new_passwd)
        user.save()
        return super().form_valid(form)

class ManagementUSRUpdate(UpdateView):
    model = User
    template_name = 'management/usr_detail.html'
    form_class = UpdateUSRForm
    success_url = reverse_lazy('management_usr_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edited_user'] = self.object
        context['user'] = self.request.user
        return context

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     #self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())


class ManagementUsrPassword(UpdateView):
    model = User
    template_name = 'management/usr_password.html'
    form_class = UpdateUsrPwdForm
    success_url = reverse_lazy('management_usr_detail')

    def get_success_url(self):
        return reverse_lazy('management_usr_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edited_user'] = self.object
        context['user'] = self.request.user
        return context

    def test_func(self):
        return self.request.user.is_superuser

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs

    def form_valid(self, form):
        user = self.get_object()
        new_passwd = form.cleaned_data['password1']
        user.set_password(new_passwd)
        user.save()
        messages.success(self.request, f"{user.username}'s Password reset successfully!")
        return HttpResponseRedirect(self.get_success_url())


class ManagementUSRDelete(DeleteView):
    model = User
    template_name = 'management/usr_delete.html'
    success_url = reverse_lazy('management_usr_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edited_user'] = self.object
        context['user'] = self.request.user
        return context

#################### My Booking
class MyBookingList(ListView):
    model = Reservation
    template_name = 'my_booking_list.html'

    def get_queryset(self):
        return Reservation.objects.filter(client=self.request.user).order_by('check_in_datetime')

class MyBookingCreate(CreateView):
    model = Reservation
    template_name = 'my_booking_create.html'
    success_url = reverse_lazy('my_booking_list')
    form_class = MyBookingCreateForm

    def form_valid(self, form):
        try:
            form.instance.creator = self.request.user
            form.instance.client = self.request.user
            self.object = form.save(commit=False)
            self.object.full_clean()
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        except ValidationError as e:
            #messages.error(self.request, e.message)
            form.add_error(None, e)
            return self.form_invalid(form)

class MyBookingUpdate(UpdateView):
    model = Reservation
    template_name = 'my_booking_detail.html'
    success_url = reverse_lazy('my_booking_list')
    form_class = MyBookingCreateForm

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.full_clean()
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

class MyBookingDelete(DeleteView):
    model = Reservation
    template_name = 'my_booking_delete.html'
    success_url = reverse_lazy('my_booking_list')


################### Book a room

class BookStep1(ListView):
    model = Room
    template_name = 'rsv_step1.html'
    # context_object_name = 'rooms'
    ordering = 'room_number'


    def get_queryset(self):
        queryset = Room.objects.all().order_by('room_number')
        startDT = self.request.GET.get('startDT')
        endDT = self.request.GET.get('endDT')

        if startDT and endDT:
            try:
                startDT = parse_datetime(startDT)
                endDT = parse_datetime(endDT)

                if startDT and endDT:
                    reserved_rooms = Reservation.objects.filter(
                        Q(check_in_datetime__lt=endDT) & Q(check_out_datetime__gt=startDT)
                    ).values_list('room_id', flat=True)

                    queryset = queryset.exclude(id__in=reserved_rooms)
            except ValueError:
                pass

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['startDT'] = self.request.GET.get('startDT', '')
        context['endDT'] = self.request.GET.get('endDT', '')
        return context
class BookStep2(CreateView):
    model = Reservation
    template_name = 'rsv_step2.html'
    success_url = reverse_lazy('my_booking_list')
    form_class = MyBookingCreateStep2Form

    def get_form_kwargs(self):
        kwargs = super(BookStep2, self).get_form_kwargs()
        kwargs.update({
            'room_id': self.kwargs['room_id'],
            'check_in': self.kwargs['check_in'],
            'check_out': self.kwargs['check_out']
        })
        print(kwargs)
        return kwargs

    def form_valid(self, form):
        try:
            form.instance.creator = self.request.user
            form.instance.client = self.request.user
            form.instance.room = self.request.room_id
            form.instance.check_in_datetime = self.request.check_in
            form.instance.check_out_datetime = self.request.check_out
            self.object = form.save(commit=False)
            self.object.full_clean()
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        except ValidationError as e:
            #messages.error(self.request, e.message)
            form.add_error(None, e)
            return self.form_invalid(form)
