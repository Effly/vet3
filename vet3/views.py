from django.db import IntegrityError
from .forms import AppointmentForm
from django.shortcuts import render, redirect
from datetime import timedelta, datetime
from .models import Appointment
import pprint


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
            pp = pprint.PrettyPrinter(indent=4)

            service = form.cleaned_data['service']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Получаем последнюю запись с тем же service
            last_appointment = Appointment.objects.filter(service=service).order_by('-date', '-time').first()
            pp.pprint(last_appointment)
            if last_appointment:
                last_datetime = datetime.combine(last_appointment.date, last_appointment.time)
                new_datetime = datetime.combine(date, time)
                pp.pprint((new_datetime - last_datetime).total_seconds())
                # Проверяем разницу во времени
                if abs((new_datetime - last_datetime).total_seconds()) < 600:  # 600 секунд = 10 минут
                    form.add_error(None, 'Разница между временем этой записи и последней записи менее 10 минут. Пожалуйста, выберите другое время.')
                    return render(request, 'appointment.html', {'form': form})

            try:
                form.save()
                return redirect('appointment_success')
            except IntegrityError:
                form.add_error(None, 'Данное время уже занято. Пожалуйста, выберите другое время.')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')