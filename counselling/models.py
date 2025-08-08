from django.db import models

# Create your models here.

from django.contrib.auth.models import User  # ✅ Import the User model

from django.db import models
from django.contrib.auth.models import User

class CareerCounselor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)
    contact_email = models.EmailField()
    
    def __str__(self):
        return self.full_name

class CareerSession(models.Model):
    counselor = models.ForeignKey(CareerCounselor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    seats_available = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.title} by {self.counselor.full_name}"


class Career(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class GuidanceSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ No more error
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    email = models.EmailField(default="nayakjhunu40@gmail.com")

    def __str__(self):
        return f"{self.user.username} - {self.career.name}"
