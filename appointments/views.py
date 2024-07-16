from django.shortcuts import render
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

def booking_confirmation(request):
    return render(request, 'appointments/booking_confirmation.html')
