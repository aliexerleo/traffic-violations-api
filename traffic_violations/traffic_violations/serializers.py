from rest_framework import serializers
from django.contrib.auth.models import User
from apps.report.models import Violation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class violationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = ['licence','date_incidence','official_comment','email']
