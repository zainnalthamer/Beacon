from django.urls import path
from .views import dashboard, instructor_dashboard, CustomLoginView, student_list, add_student

urlpatterns = [
   path('auth/login/', CustomLoginView.as_view(), name='login'),
   path('dashboard/', dashboard, name='dashboard'),
   path('instructor-dashboard/', instructor_dashboard, name='instructor_dashboard'),
   path('students/', student_list, name='student_list'),
   path('students/add/', add_student, name='add_student'),
]