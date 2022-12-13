from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = student
        fields = '__all__'