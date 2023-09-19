from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

def add_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/add_ticket.html', {'form': form})

def tickets_list(request):
    tickets = Ticket.objects.all().order_by('-creation_date')
    return render(request, 'tickets/tickets_list.html', {'tickets': tickets})


from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('tickets_list')
    return render(request, 'tickets/login.html', {})

@login_required
def tickets_list(request):
    ...