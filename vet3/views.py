from django.shortcuts import render, redirect
from .forms import AppointmentForm
def home(request):
    return render(request, 'main.html')

def appointment(request):
    return render(request, 'appointment.html')

def services(request):
    return render(request, 'services.html')

def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')