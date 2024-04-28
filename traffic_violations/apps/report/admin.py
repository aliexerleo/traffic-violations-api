from django.contrib import admin
from apps.report.models import Person, Vehicle, Violation
# Register your models here.
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Violation)


