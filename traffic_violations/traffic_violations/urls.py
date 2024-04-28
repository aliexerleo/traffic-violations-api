"""
URL configuration for traffic_violations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.report import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url  person
    path('', views.list_persons, name='list_persons'),
    path('delete/<int:id>', views.delete_person, name='delete_person'),
    path('addPerson/', views.create_person, name='add_person'),
    path('edit/<int:id>', views.update_person, name='edit_person'),
    path('editing/', views.updating_person, name='editing_person'),

    # url  official
    path('official/', views.list_official, name='list_official'),
    path('deleteOfficial/<int:id>', views.delete_official, name='delete_official'),
    path('editOfficial/<int:id>', views.update_official, name='edit_official'),
    path('editingOfficial/', views.updating_official, name='editing_official'),

    # url  vehicle
    path('vehicle/', views.list_vehicle, name='list_vehicle'),
    path('deleteVehicle/<int:id>', views.delete_vehicle, name='delete_vehicle'),
    path('addVehicle/', views.create_vehicle, name='add_vehicle'),
    path('editVehicle/<int:id>', views.update_vehicle, name='edit_vehicle'),
    path('editingVehicle/', views.updating_vehicle, name='editing_vehicle'),

]
