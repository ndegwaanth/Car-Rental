from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from myapp.form import ClientForm
from django.contrib import messages
from myapp.functions.functions import handle_uploaded_file


def hello(request):
    return HttpResponse("<h1>Welcome back Tony</>")


def register(request):
    if request.method == "POST":
        client = ClientForm(request.POST, request.FILES)

        if client.is_valid():
            try:
                # Save the form data to the database
                client.save()

                # Add a success message
                messages.success(request, "Data validation was successful!")

                # Handle the uploaded file (if necessary)
                handle_uploaded_file(request.FILES['file'])

                # Redirect to the homepage after successful registration
                return redirect('homepage')
            except Exception as e:
                # Catch any exception and show an error message
                messages.error(request, f"Error saving the form: {e}")
        else:
            messages.error(request, "The form data is not valid.")
    else:
        client = ClientForm()

    return render(request, "register.html", {'form': client})

def homepage(request):
    return render(request, "homepage.html")

def index(request):
    context = {
        'name': {
            'CUK': "BSIT",
            'CUK1': "BSIT1",
            'CUK2': "BSIT2",
            'CUK3': "BSIT3",
            'CUK4': "BSIT4",
            'CUK5': "BSIT5"
        }
    }
    return render(request, "index.html", context)