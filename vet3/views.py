# vet3/views.py

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .forms import AppointmentForm
from .models import Appointment

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
            service = form.cleaned_data['service']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Проверка последней записи для услуги и даты/времени
            last_appointment = Appointment.objects.filter(service=service, date=date).order_by('-time').first()
            if last_appointment:
                time_difference = timezone.now().time() - last_appointment.time
                if time_difference < timedelta(minutes=10):
                    form.add_error('time', 'Запись невозможна. Прошло менее 10 минут с последней записи.')
                    return render(request, 'appointment.html', {'form': form})

            try:
                form.save()
                return redirect('appointment_success')
            except IntegrityError:
                form.add_error('error', 'Данное время уже занято. Пожалуйста, выберите другое время.')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')
