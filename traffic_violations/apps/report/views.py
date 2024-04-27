from django.shortcuts import (redirect,
                              render,
                              HttpResponseRedirect)
# Create your views here.
from apps.report.models import Person

# logic to create person
def create_person(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    person = Person.objects.create(name=name, email=email)
    return redirect('/')


# logic to list person
def list_persons(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
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
    return render(request, "add_person.html", {})

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

