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

