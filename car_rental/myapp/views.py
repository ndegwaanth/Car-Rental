from django.shortcuts import render
from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("<h1>Welcome back Tony</>")


def index(request):
    now_date = datetime.datetime.now()
    html = f"<h1>What time is it now {now_date}</>"

    return HttpResponse(html)
