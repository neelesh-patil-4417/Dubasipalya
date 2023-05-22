from django.shortcuts import render
from base.models import schedule
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import schedule
from datetime import datetime,timedelta
from pytz import timezone


@api_view(["GET"])
def home(request):
    arrival_times = schedule.objects.values_list("arrives",flat=True)
    at = []
    for i in arrival_times:
        at.append(str(i))
    
    ct = datetime.now(timezone('UTC')).astimezone(timezone('Asia/Kolkata')).time()
    ct_str = ct.strftime("%H:%M:%S")
    print(ct_str)
    end_time = (datetime.combine(datetime.today(), ct) + timedelta(hours=1)).time()
    et_str = end_time.strftime("%H:%M:%S")
    print(et_str)
    available_trains = [time for time in at if ct_str <= time <= et_str]
    context = {
        "available_trains": available_trains
    }

    return render(request,"home.html",context=context)
