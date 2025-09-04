from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import User, Assignment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
import requests
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django import forms
from .forms import AddStudentForm, AssignmentForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user

        if user.role == user.Role.INSTRUCTOR:
            return reverse_lazy('instructor_dashboard')
        
        return reverse_lazy('dashboard')
    
# Dashboard View
def dashboard(request):
    return render(request, 'dashboard.html', {'role': request.user.role}) # load dashboard

def is_instructor(u): return u.role == u.Role.INSTRUCTOR
def is_student(u): return u.role == u.ROLE_STUDENT

@login_required
@user_passes_test(is_instructor)
def instructor_dashboard(request):
    instructors = User.objects.filter(role=User.Role.INSTRUCTOR)
    return render(request, 'instructors/instructor_dashboard.html', {'instructors':instructors})

@login_required
@user_passes_test(is_instructor)
def student_list(request):
    students = User.objects.filter(role=User.Role.STUDENT)
    return render(request, 'students/student_list.html', {'students': students})

@login_required
@user_passes_test(is_instructor)
def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = AddStudentForm()
    return render(request, 'students/add_student.html', {'form': form})

@login_required
@user_passes_test(is_instructor)
def student_detail(request, pk):
    student = User.objects.get(pk=pk, role=User.Role.STUDENT)
    return render(request, 'students/student_detail.html', {'student': student})

@login_required
@user_passes_test(is_instructor)
def delete_student(request, pk):
    student = User.objects.get(pk=pk, role=User.Role.STUDENT)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_list.html', {'student': student})

@login_required
@user_passes_test(is_instructor)
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

@login_required
@user_passes_test(is_instructor)
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'assignments/add_assignment.html', {'form': form})

@login_required
@user_passes_test(is_instructor)
def assignment_detail(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    return render(request, 'assignments/assignment_detail.html', {'assignment': assignment})