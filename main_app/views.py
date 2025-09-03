from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
import requests
    
# Dashboard View
def dashboard(request):
    return render(request, 'dashboard.html', {'role': request.user.role}) # load dashboard

def is_instructor(u): return u.role == u.Role.INSTRUCTOR
def is_student(u): return u.role == u.ROLE_STUDENT

@login_required
@user_passes_test(is_instructor)
def any_function(request):
    pass

# # STUDENT VIEWS
# def student_list(request):
#     students = User.objects.filter(role=User.Role.STUDENT)
#     return render(request, 'students/student_list.html', {'students': students})