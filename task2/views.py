from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import student


def mainPage_function(request):
    return render(request, 'task2/mainPage.html')


def students(request):
    students = student.objects.all()
    context = {'students':students}
    return render(request,'task2/students.html' ,context)

def single_student(request,pk):
    studentObj = student.objects.get(id=pk)
    form = StudentForm()

    if request.method == 'POST':
        form = form(request.POST)
        return redirect('project', pk=studentObj.id)

    return render(request, 'task2/single-Student.html', {'student': studentObj, 'form': form})


def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    context = {'form': form}
    return render(request, 'task2/task3_form.html', context)

def update_student(request,pk):
    studentObj = student.objects.get(id=pk)
    form = StudentForm(instance=studentObj)

    if request.method == 'POST':
        form = StudentForm(request.POST , instance=studentObj)
        if form.is_valid():
            form.save()
            return redirect('students')
    context = {'form': form}
    return render(request, 'task2/task3_form.html', context)

def delete_student(request,pk):
    studentObj = student.objects.get(id=pk)
    if request.method == 'POST':
        studentObj.delete()
        return redirect('students')

    context = {'object' : studentObj}
    return render(request,'task2/delete_student.html',context)