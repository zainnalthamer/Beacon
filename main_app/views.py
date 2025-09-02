from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test

def is_instructor(u): return u.role == u.Role.INSTRUCTOR
def is_student(u): return u.role == u.ROLE_STUDENT

@login_required
@user_passes_test(is_instructor)
def any_function(request):
    pass