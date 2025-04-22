"""
URL configuration for Task2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from TWRL.views import *

urlpatterns = [
    path('', index, name="index"),
    path("register/", register, name='register'),
    path("roomlist/", RoomList.as_view(), name='room_list'),
    path("management/roomlist/", ManagementRoomList.as_view(), name='management_room_list'),
    path("management/roomcreate/", ManagementRoomCreate.as_view(), name='management_room_create'),
    path("management/roomdetail/<int:pk>", ManagementRoomUpdate.as_view(), name='management_room_detail'),

    #Don't Use this Booking entry for now
    #path("management/roomBook/<int:pk>", ManagementRoomBook.as_view(), name='management_room_book'),
    path("management/roomdelete/<int:pk>", ManagementRoomDelete.as_view(), name='management_room_delete'),
    path("management/rsvlist/", ManagementRSVList.as_view(), name='management_rsv_list'),
    path("management/rsvcreate/", ManagementRSVCreate.as_view(), name='management_rsv_create'),
    path("management/rsvdetail/<int:pk>", ManagementRSVUpdate.as_view(), name='management_rsv_detail'),
    path("management/rsvdelete/<int:pk>", ManagementRSVDelete.as_view(), name='management_rsv_delete'),
]
