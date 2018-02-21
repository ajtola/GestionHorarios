from schedule.models import Schedule
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
import datetime

# Create your views here.
def schedule_table(request):
    if request.POST:
        val = request.POST.get('start_finish')
        if val == "start":
            start_button(request)
        else:
            finish_button(request, val)
                
    worker_id = User.objects.get(username__exact=request.user.username)
    today = datetime.date.today()
    schedules = Schedule.objects.filter(worker__exact=worker_id, start__year=today.year, start__month=today.month)
    return render(request, 'schedule/schedule_table.html', {'schedules': schedules})

def finish_button(request, schedule_id):
    finish_date = timezone.now()
    sch = Schedule.objects.get(id=schedule_id)
    sch.finish = finish_date
    sch.save()
    setHoursWorked(schedule_id)
    #Show_table
    '''worker_id = User.objects.get(username__exact=request.user.username)
    schedules = Schedule.objects.filter(worker__exact=worker_id)
    return render(request, 'schedule/schedule_table.html', {'schedules': schedules})'''


def start_button(request):
    schedule = Schedule()
    schedule.start = timezone.now()
    schedule.finish = None
    schedule.worker = User.objects.get(username__exact=request.user.username)
    schedule.save()

#Servicios
def setHoursWorked(schedule_id):
    sch = Schedule.objects.get(id=schedule_id)
    start = sch.start
    finish = sch.finish
    hoursWorked = finish - start
    sch.hours_worked = hoursWorked
    sch.save()
    