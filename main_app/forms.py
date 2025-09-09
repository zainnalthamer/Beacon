from django import forms
from .models import User, Assignment, Submission, Feedback, Classroom

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user
    
class AddStudentForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.STUDENT
        user.username = f"{user.first_name.lower()}.{user.last_name.lower()}"
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        
        return user
    
class AssignmentForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Assignment
        fields = ['title', 'assignment_type', 'classroom', 'deadline', 'repo_url', 'technology']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["repo_url", "live_url", "win", "challenge", "assistance", "cover_image"]

    def __init__(self, *args, **kwargs):
        self.assignment = kwargs.pop("assignment", None)
        super().__init__(*args, **kwargs)

        self.fields["repo_url"].required = True
        self.fields["live_url"].required = True
        self.fields["win"].required = False
        self.fields["challenge"].required = False
        self.fields["assistance"].required = False

        if self.assignment and getattr(self.assignment, "assignment_type", None) == self.assignment.AssignmentType.PROJECT:
            self.fields["cover_image"].required = True  
        else:
            self.fields["cover_image"].required = False

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comments']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name']

class AddStudentToClassroomForm(forms.Form):
    student = forms.ModelChoiceField(queryset=User.objects.filter(role=User.Role.STUDENT, classroom__isnull=True))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']