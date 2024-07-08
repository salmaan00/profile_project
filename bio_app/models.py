from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.portfolio.user.username}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    work_experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(blank=True)
   

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)