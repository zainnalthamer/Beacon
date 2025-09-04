from django.urls import path
from .views import (dashboard, instructor_dashboard, CustomLoginView, 
                    student_list, add_student, student_detail, delete_student,
                    assignment_list, add_assignment, assignment_detail, edit_assignment, delete_assignment,
                    submit_assignment, submission_detail
                    )

urlpatterns = [
   path('auth/login/', CustomLoginView.as_view(), name='login'),
   path('dashboard/', dashboard, name='dashboard'),

   path('instructor-dashboard/', instructor_dashboard, name='instructor_dashboard'),
   path('students/', student_list, name='student_list'),
   path('students/add/', add_student, name='add_student'),
   path('students/<int:pk>/', student_detail, name='student_detail'),
   path('students/<int:pk>/delete/', delete_student, name='delete_student'),
   path('assignments/', assignment_list, name='assignment_list'),
   path('assignments/add/', add_assignment, name='add_assignment'),
   path('assignments/<int:pk>/', assignment_detail, name='assignment_detail'),
   path('assignments/<int:pk>/edit/', edit_assignment, name='edit_assignment'),
   path('assignments/<int:pk>/delete/', delete_assignment, name='delete_assignment'),
   path('submissions/<int:pk>/', submission_detail, name='submission_detail'),

   path('assignments/<int:pk>/submit/', submit_assignment, name='submit_assignment'),
]