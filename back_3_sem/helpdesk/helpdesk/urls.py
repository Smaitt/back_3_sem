from django.contrib import admin
from django.urls import path, include
from tickets.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_view, name='login_view'),
    path('add_ticket/', add_ticket, name='add_ticket'),
    path('list/', tickets_list, name='tickets_list'),
     path('', home, name='home'),
]
