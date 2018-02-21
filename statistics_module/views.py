from django.shortcuts import render
from statistics_module.forms import SearchingForm
from schedule.models import Schedule
from django.http.response import HttpResponse
import json
import datetime

# Create your views here.
def statistics_home(request):
    form = SearchingForm()
    return render(request, 'statistics_module/statistics_home.html', {'form':form})

def statistics_result(request):
    form = SearchingForm()
    if request.method=='POST':
        form = SearchingForm(request.POST)
        if form.is_valid():
            cd = "a"
    
def statistics_search(request):
    year = request.POST.get('A')
    month = request.GET.get('M')
    day = request.GET.get('D')
    query = Schedule.objects
    if year is not None:
        query = query.filter(start__year=year)
    if month is not None:
        query = query.filter(start__month=month)
    if day is not None:
        query = query.filter(start__day=day)   
    schedules = [ statistics_search_serializer(sch) for sch in query.all() ] 
    return HttpResponse(json.dumps(schedules, default = myconverter), content_type='application/json')

def statistics_search_serializer(schedules):
    return {'Id': schedules.id, 'Start': schedules.start, 'Finish': schedules.finish}

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()