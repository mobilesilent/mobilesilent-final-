from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    user_type = models.CharField(max_length=50,null=True,blank=True)
    
class StudentTable(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    admission_no = models.CharField(max_length=30,null=True,blank=True)
    department = models.CharField(max_length=30,null=True,blank=True)
    class_name = models.CharField(max_length=30,null=True,blank=True)
    semester = models.CharField(max_length=30,null=True,blank=True)
    email_id = models.CharField(max_length=30,null=True,blank=True)
    phone_no = models.BigIntegerField(null=True,blank=True)
    LOGIN=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

class ClassroomTable(models.Model):
    department = models.CharField(max_length=30,null=True,blank=True)
    className = models.CharField(max_length=30,null=True,blank=True)
    roomNumber=models.IntegerField(null=True,blank=True)

class Timing(models.Model):
    subject = models.CharField(max_length=30,null=True,blank=True)
    day = models.CharField(max_length=30,null=True,blank=True)
    to = models.TimeField(max_length=20,null=True,blank=True)
    start= models.TimeField(max_length=20,null=True,blank=True)

class FeedbackTable(models.Model):
    user_id = models.ForeignKey(StudentTable,on_delete=models.CASCADE,max_length=30,null=True,blank=True)
    feedback = models.CharField(max_length=30,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

class ComplaintTable(models.Model):
    user_id = models.ForeignKey(StudentTable,on_delete=models.CASCADE,null=True,blank=True)
    complaints = models.CharField(max_length=30,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    reply = models.CharField(max_length=30,null=True,blank=True)

class TeacherTable(models.Model):
    login_id =models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    name =models.CharField(max_length=30,null=True,blank=True)
    department =models.CharField(max_length=30,null=True,blank=True)
    email =models.CharField(max_length=30,null=True,blank=True)
    phone_no =models.BigIntegerField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    class_name = models.CharField(max_length=30,null=True,blank=True)


class DepartmentTable(models.Model):
    department=models.CharField(max_length=30,null=True,blank=True)



