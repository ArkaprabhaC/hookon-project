from django.db import models

from django.utils import timezone

# Create your models here.


class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_email = models.EmailField(max_length=50)
    s_password = models.TextField(max_length=20)
    s_name = models.TextField(max_length=300)
    s_dob= models.DateField()
    s_phone= models.BigIntegerField()
    s_skills= models.TextField(max_length=500)
    s_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.s_name

class Interns(models.Model):
    track_id = models.AutoField(primary_key=True)
    i_id = models.IntegerField()
    r_id = models.IntegerField()
    s_id= models.IntegerField()

    def __self__ (self):
        return self.track_id

class Recruiter(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_email = models.EmailField(max_length=50)
    r_password = models.TextField(max_length=20)
    r_name = models.CharField(max_length=300)
    r_dob = models.DateField()
    r_phone = models.BigIntegerField()
    r_company = models.TextField(max_length=500)
    r_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.r_name

class Internships(models.Model):
    i_id = models.AutoField(primary_key=True)
    i_company = models.CharField(max_length=100)
    i_logo = models.ImageField(upload_to='images/logo')
    i_category= models.CharField(max_length=50)
    i_skills= models.TextField()
    i_number= models.IntegerField()
    i_desc= models.TextField(max_length=400)
    i_location= models.CharField(max_length=20)

    def __str__(self):
        internship= self.i_company + " " + self.i_category
        return internship
