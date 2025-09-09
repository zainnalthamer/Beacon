from django.urls import path
from .views import (dashboard, instructor_dashboard, CustomLoginView, 
                    student_list, add_student, student_detail, delete_student,
                    assignment_list, add_assignment, assignment_detail, edit_assignment, delete_assignment,
                    submit_assignment, submission_detail,
                    classroom_list, add_classroom, delete_classroom, manage_classroom_students, add_student_to_classroom, remove_student_from_classroom,
                    discover_projects, delete_submission, profile, edit_profile, instructor_student_profile
                    )
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
   path('auth/login/', CustomLoginView.as_view(), name='login'),
   path('dashboard/', dashboard, name='dashboard'),
   path('discover/', discover_projects, name='discover_projects'),
   path('profile/', profile, name='profile'),
   path('profile/edit/', edit_profile, name='edit_profile'),
   path('profile/change-password/', auth_views.PasswordChangeView.as_view(
        template_name='change_password.html',
        success_url=reverse_lazy('profile')
    ), name='change_password'),

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
   path('classrooms/', classroom_list, name='classroom_list'),
   path('classrooms/add/', add_classroom, name='add_classroom'),
   path('classrooms/<int:pk>/delete/', delete_classroom, name='delete_classroom'),
   path('classrooms/<int:pk>/manage/', manage_classroom_students, name='manage_classroom_students'),
   path('classrooms/<int:pk>/add_student/', add_student_to_classroom, name='add_student_to_classroom'),
   path('classrooms/<int:pk>/remove_student/<int:student_pk>/', remove_student_from_classroom, name='remove_student_from_classroom'),

   path('assignments/<int:pk>/submit/', submit_assignment, name='submit_assignment'),
   path('submissions/<int:pk>/delete/', delete_submission, name='delete_submission'),
   path('students/<int:pk>/profile/', instructor_student_profile, name='instructor_student_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)