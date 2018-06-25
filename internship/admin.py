from django.contrib import admin
from .models import Student, Interns,Recruiter,Internships
# Register your models here.

admin.site.register(Student)
admin.site.register(Interns)
admin.site.register(Recruiter)
admin.site.register(Internships)