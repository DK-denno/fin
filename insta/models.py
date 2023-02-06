from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField
# Create your models here.


class Stream(models.Model):
    name = models.CharField(max_length=1)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']

    @classmethod
    def save_stream(self):
        self.save()

    @classmethod
    def get_stream(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def delete_stream(self):
        self.delete()

class Classes(models.Model):
    name = models.CharField(max_length=1)
    classTeacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='class+')
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name="classes")
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']

    @classmethod
    def save_stream(self):
        self.save()

    @classmethod
    def get_stream(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def delete_stream(self):
        self.delete()

GENDER_CHOICES = (
    ('male','Male'),
    ('female', 'Female'),
)

ROLES = (
    ('staff','Staff'),
    ('student', 'Student'),
)
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    dp = ImageField(blank=True, manual_crop="")
    bio = HTMLField(max_length=500)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    role = models.CharField(choices=ROLES, max_length=10)
    email_confirmed = models.BooleanField(default=False)
    classes = models.ForeignKey(Classes, blank=True, on_delete=models.CASCADE, related_name="profile")
    regNumber = models.CharField(max_length=20)
    createdOn = models.DateTimeField(auto_now_add=True)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username
