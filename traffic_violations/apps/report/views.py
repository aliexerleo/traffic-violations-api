from django.shortcuts import (redirect,render)
# Create your views here.
from apps.report.models import Person, Official

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
    context["dataset"] = Official.objects.all()
    return render(request, "list_official.html", context)

def delete_official(request, id):
    official = Official.objects.get(id=id)
    official.delete()
    return redirect('/official/')

def create_official(request):
    if request.method == "POST":
        name = request.POST.get('name')
        id_number = request.POST.get('number')
        official = Official.objects.create(name=name, id_number=id_number)
        return redirect('/official/')
    return render(request, "list_official.html", {})

def update_official(request, id):
    official = Official.objects.get(id=id)
    data = {
        'official': official
    }
    return render(request, "update_official.html", data)

def updating_official(request):
    id = int(request.POST.get('id'))
    name = request.POST.get('name')
    id_number = request.POST.get('id_number')
    official = Official.objects.get(id=id)
    official.name = name
    official.id_number = id_number
    official.save()
    return redirect('/official')
