from django.shortcuts import (redirect,render)
# Create your views here.
# import django user model
from django.contrib.auth.models import User
from apps.report.models import Person, Vehicle

# persons
def list_persons(request):
    context ={}
    context["dataset"] = Person.objects.all()
    return render(request, "list_persons.html", context)

def delete_person(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('/')

def create_person(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        person = Person.objects.create(name=name, email=email)
        return redirect('/')
    return render(request, "list_persons.html", {})

def update_person(request, id):
    person = Person.objects.get(id=id)
    data = {
        'person': person
    }
    return render(request, "update_persons.html", data)

def updating_person(request):
    id = int(request.POST.get('id'))
    name = request.POST.get('name')
    email = request.POST.get('email')
    person = Person.objects.get(id=id)
    person.name = name
    person.email = email
    person.save()
    return redirect('/')

# officcial
def list_official(request):
    context ={}
    context["dataset"] = User.objects.all()
    return render(request, "list_official.html", context)

def delete_official(request, id):
    official = User.objects.get(id=id)
    official.delete()
    return redirect('/official/')

def create_official(request):
    if request.method == "POST":
        name = request.POST.get('username')
        official = User.objects.create(username=name)
        return redirect('/official/')
    return render(request, "list_official.html", {})

def update_official(request, id):
    official = User.objects.get(id=id)
    print(official)
    data = {
        'official': official
    }
    return render(request, "update_official.html", data)

def updating_official(request):
    id = int(request.POST.get('id'))
    name = request.POST.get('name')
    print(name)
    official = User.objects.get(id=id)
    official.username = name
    official.save()
    return redirect('/official')

# vehicles
def list_vehicle(request):
    person = Person.objects.all()
    vehicle = Vehicle.objects.all()
    context ={
        'person': person,
        'vehicle': vehicle
    }
    return render(request, "list_vehicle.html", context)

def delete_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    return redirect('/vehicle/')

def create_vehicle(request):
    if request.method == "POST":
        person = request.POST.get('person')
        vehicle_number = request.POST.get('vehicle_number')
        vehicle_type = request.POST.get('vehicle_type')
        vehicle_color = request.POST.get('vehicle_color')
        vehicle = Vehicle.objects.create(vehicle_number=vehicle_number, vehicle_type=vehicle_type, vehicle_color=vehicle_color, person_id=person)
        return redirect('/vehicle/')
    return render(request, "list_vehicle.html", {})

def update_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    data = {
        'vehicle': vehicle
    }
    return render(request, "update_vehicle.html", data)

def updating_vehicle(request):
    id = request.POST.get('id')
    vehicle_number = request.POST.get('vehicle_number')
    vehicle_type = request.POST.get('vehicle_type')
    vehicle_color = request.POST.get('vehicle_color')
    vehicle = Vehicle.objects.get(id=id)
    vehicle.vehicle_number = vehicle_number
    vehicle.vehicle_type = vehicle_type
    vehicle.vehicle_color = vehicle_color
    vehicle.save()
    return redirect('/vehicle')
