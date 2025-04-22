from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from TWRL.forms import *
from TWRL.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    # if request.method == 'POST':
    #     username=request.POST['username']
    #     email = request.POST['email']
    #     fname = request.POST['firstname']
    #     lname = request.POST['lastname']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']
    #     if password == password2:
    #         user = User.objects.create_user(username=username, email=email, first_name=fname, last_name=lname)
    #         user.set_password(password)
    #         user.save()
    #         return redirect('login')

    return render(request, 'register.html')


class RoomList(ListView):
    model = Room
    template_name = 'roomlist.html'

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
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ManagementRoomUpdate(UpdateView):
    model = Room
    template_name = 'management/roomdetail.html'
    form_class = CreateRoomForm
    success_url = reverse_lazy('management_room_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ManagementRoomBook(CreateView):
    model = Reservation
    template_name = 'management/rsvcreate.html'
    fields = ['client', 'creator', 'title', 'desc']
    success_url = reverse_lazy('management_rsvDetail_create')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ManagementRoomDelete(DeleteView):
    model = Room
    template_name = 'management/roomdelete.html'
    success_url = reverse_lazy('management_room_list')

class ManagementRSVList(ListView):
    model = Reservation
    template_name = 'management/rsvlist.html'

class ManagementRSVCreate(CreateView):
    model = Reservation
    template_name = 'management/rsvcreate.html'
    #fields = ['title', 'client', 'desc']
    success_url = reverse_lazy('management_rsv_list')
    form_class = CreateRSVForm

    def form_valid(self, form):
        try:
            form.instance.creator = self.request.user
            self.object = form.save(commit=False)
            self.object.user = self.request.user
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
            self.object.user = self.request.user
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