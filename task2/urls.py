from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage_function),
    path('students', views.students, name='students'),
    path('single_student<str:pk>', views.single_student, name='single_student'),
    path('add-student', views.add_student, name='add-student'),
    path('update-student<str:pk>', views.update_student, name='update-student'),
    path('delete-student<str:pk>', views.delete_student, name='delete-student')

]
