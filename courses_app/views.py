from django.shortcuts import render, redirect

from .models import *

from django.contrib import messages

def index(request):
    context = {
        "courses": Course.objects.all(),
        "descriptions": Description.objects.all()
    }
    return render(request, 'index.html', context)

def destroy(request, desc_id):
    context = {
        "course": Description.objects.get(id=desc_id),
    }
    return render(request, 'destroy.html', context)

def add_course(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        errors = Description.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:        
            new_course = Course.objects.create(name=request.POST['name'])
            Description.objects.create(desc=request.POST['desc'],course=Course.objects.get(id=new_course.id))
            return redirect('/')

def destroy_course(request):
    if request.method == 'POST':
        course_to_destroy = Course.objects.get(id=request.POST['course_id'])
        course_to_destroy.delete()
        return redirect('/')