from django.db import models

from django.utils import timezone

# Create your models here.


class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_email = models.EmailField(max_length=50)
    s_password = models.CharField(max_length=20)
    s_name = models.TextField(max_length=300)
    s_dob= models.DateField()
    s_phone= models.BigIntegerField()
    s_skills= models.TextField(max_length=500)
    s_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.s_name

class Recruiter(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_email = models.EmailField(max_length=50)
    r_password = models.CharField(max_length=20)
    r_name = models.CharField(max_length=300)
    r_dob = models.DateField()
    r_phone = models.BigIntegerField()
    r_company = models.TextField(max_length=500)
    r_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.r_name

class Internship(models.Model):
    i_id = models.AutoField(primary_key=True)
    i_company = models.CharField(max_length=100)
    i_logo = models.ImageField(upload_to='images/logo/')
    i_category= models.CharField(max_length=50)
    i_skills= models.TextField()
    i_number= models.IntegerField()
    i_desc= models.TextField(max_length=400)
    i_location= models.CharField(max_length=20)

    def __str__(self):
        internship= self.i_company + " " + self.i_category
        return internship

class Intern(models.Model):
    track_id = models.AutoField(primary_key=True)
    i= models.ForeignKey(Internship,on_delete=models.CASCADE)
    r= models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    s= models.ForeignKey(Student,on_delete=models.CASCADE)
    def __self__ (self):
        return self.track_id

class Ad(models.Model):
    ad_id=models.AutoField(primary_key=True)
    ad_img=models.ImageField(upload_to='images/ads/')
    ad_name=models.CharField(max_length=50)
    ad_desc=models.TextField(max_length=250)
    def __self__ (self):
        return self.ad_name

class Course(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_img=models.ImageField(upload_to='images/ads/')
    c_name=models.CharField(max_length=50)
    c_desc=models.TextField(max_length=250)
    c_link=models.TextField(max_length=100)
    def __self__ (self):
        return self.c_name