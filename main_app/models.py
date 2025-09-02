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

# Technology model
class Technology(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    logo_image = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# Project model
class Project(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    repo_url = models.CharField(max_length=255)
    project_url = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='project_covers/', null=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title
    
# ProjectContributor model
class ProjectContributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributions')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')

    def __str__(self):
        return f"{self.user.username} → {self.project.title}"
    
# Bookmark model
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bookmarked_by')

    def __str__(self):
        return f"{self.user.username} bookmarked {self.project.title}"