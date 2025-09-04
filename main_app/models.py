from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# User model
class User(AbstractUser):
    class Role(models.TextChoices):
        INSTRUCTOR = "instructor", "Instructor"
        STUDENT = "student", "Student"

    role = models.CharField(
        max_length = 20,
        choices = Role.choices,
        default = Role.STUDENT,
    )

    classroom = models.ForeignKey('Classroom', on_delete=models.SET_NULL, related_name='students', null=True)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.username

# Classroom Model
class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# ClassroomInstructor Model
class ClassroomInstructor(models.Model):
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="classrooms",
        limit_choices_to={'role':'instructor'}
    )

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name = 'instructors'
    )

    class Meta:
        db_table = "classroom_instructor"

    def __str__(self):
        return f"{self.instructor.username} : {self.classroom.name}"


# Technology model
class Technology(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    logo_image = models.CharField(max_length=255)

    class Meta:
        db_table = "technology"

    def __str__(self):
        return self.name
    
# Assignment model
class Assignment(models.Model):
    class AssignmentType(models.TextChoices):
        HOMEWORK = "homework", "Homework"
        PROJECT = "project", "Project"

    title = models.CharField(max_length=80)
    assignment_type = models.CharField(
        max_length=20,
        choices=AssignmentType.choices,
        default=AssignmentType.HOMEWORK,
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name="assignments"
    )
    deadline = models.DateField()
    repo_url = models.CharField(max_length=255)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='assignments')

    class Meta:
        db_table = "assignment"

    def __str__(self):
        return f"{self.title} ({self.assignment_type})"
    
# Submission Model
class Submission(models.Model):
    class HomeworkStatus(models.TextChoices):
        COMPLETE = "complete", "Complete"
        INCOMPLETE = "incomplete", "Incomplete"
        NOT_SUBMITTED = "not_submitted", "Not Submitted"

    class ProjectStatus(models.TextChoices):
        PASS = "pass", "Pass"
        FAIL = "fail", "Fail"

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions", limit_choices_to={'role': 'student'})
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    submitted_at = models.DateTimeField(auto_now_add=True)
    repo_url = models.URLField(null=True)
    live_url = models.URLField(null=True)
    status = models.CharField(max_length=20, null=True) 

    class Meta:
        db_table = "submission"

    def __str__(self):
        return f"{self.student.username} : {self.assignment.title}"
    
# Feedback Model
class Feedback(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="feedback")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})
    comments = models.TextField()
    given_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "feedback"

    def __str__(self):
        return f"Feedback by {self.instructor.username} on {self.submission}"
    
# Bookmark Model
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='bookmarked_by', null=True,)

    class Meta:
        db_table = "bookmark"
    
    def __str__(self):
        return f"{self.user.username} bookmarked {self.assignment.title}"