from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import*

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password']

    
def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    password_confirm = cleaned_data.get("password_confirm")

    if password != password_confirm:
        raise forms.ValidationError("Passwords do not match")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'skills', 'contact']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your bio',
                'rows': 5
            }),
            'skills': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your skills'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your contact details'
            }),
        }

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['work_experience', 'education', 'certifications']
        widgets = {
            'work_experience': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your work experience',
                'rows': 5
            }),
            'education': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your education details',
                'rows': 5
            }),
            'certifications': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your certifications',
                'rows': 5
            }),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project description',
                'rows': 5
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project link'
            }),
        }