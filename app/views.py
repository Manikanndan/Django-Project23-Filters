from django.shortcuts import render
from datetime import date
# Create your views here.
date=date.today()

def filters(request):
    d={'data':'hai PYTHon','date1':date,'count':1}
    return render(request,'filters.html',d)

def fun_userfilter(request):
    d={'data':'hai PYTHon hai'}
    return render(request,'userfilter.html',d)