from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import User, Assignment, Submission, Feedback
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
import requests
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django import forms
from .forms import AddStudentForm, AssignmentForm, SubmissionForm, FeedbackForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == user.Role.INSTRUCTOR:
            return reverse_lazy('instructor_dashboard')
        elif user.role == user.Role.STUDENT:
            return reverse_lazy('dashboard')
        return reverse_lazy('login')

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
    return render(request, 'assignments/add_assignment.html', {'form': form, 'is_edit': False})

@login_required
@user_passes_test(is_instructor)
def assignment_detail(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    submissions = assignment.submissions.all()

    return render(request, 'assignments/assignment_detail.html', {'assignment': assignment, 'submissions': submissions})

@login_required
@user_passes_test(is_instructor)
def edit_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_detail', pk=assignment.pk)
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'assignments/add_assignment.html', {'form': form, 'assignment': assignment, 'is_edit': True})

@login_required
@user_passes_test(is_instructor)
def delete_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)

    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')
    return render(request, 'assignments/assignment_list.html', {'assignment': assignment})

# STUDENT VIEWS
@login_required
def dashboard(request):
    if request.user.role == request.user.Role.STUDENT:
        classroom = request.user.classroom
        submitted_assignment_ids = Submission.objects.filter(student=request.user).values_list('assignment_id', flat=True)
        assignments = Assignment.objects.filter(classroom=classroom).exclude(pk__in=submitted_assignment_ids)
        return render(request, 'students/dashboard.html', {'role': request.user.role, 'assignments': assignments})
    else:
        return render(request, 'dashboard.html', {'role': request.user.role})

@login_required
@user_passes_test(is_student)
def submit_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            return redirect('assignment_detail', pk=assignment.pk)
        else:
            form = SubmissionForm()
        return render(request, 'assignments/submit_assignment.html', {'form': form, 'assignment': assignment})
    
@login_required
def submission_detail(request, pk):
    submission = Submission.objects.get(pk=pk)
    feedback = submission.feedback.first()

    if request.user.role == request.user.Role.INSTRUCTOR:
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                fb = form.save(commit=False)
                fb.submission = submission
                fb.instructor = request.user
                fb.save()
                return redirect('submission_detail', pk=submission.pk)
            else:
                form = FeedbackForm()
        else:
            form = None
        return render(request, 'assignments/submission_detail.html', {
        'submission': submission,
        'feedback': feedback,
        'form': form,
        })