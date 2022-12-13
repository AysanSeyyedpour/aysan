from django.contrib import admin
from .models import student,content, course, registration
# Register your models here.

admin.site.register([student,content, course, registration])