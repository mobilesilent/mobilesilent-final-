from django.forms import ModelForm
from mobilesilentapp.models import *

class StuentForm(ModelForm):
    class Meta:
        model=StudentTable
        fields=['name','admission_no','department','semester','email_id','phone_no']
class ClassroomForm(ModelForm):
    class Meta:
        model=ClassroomTable
        fields=['department','className','roomNumber']
class TimingForm(ModelForm):
    class Meta:
        model=Timing
        fields=['day','start','to','subject']
class FeedbackForm(ModelForm):
    class Meta:
        model=FeedbackTable
        fields=['feedback']
class ComplaintsForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['complaints']
class TeacherregistrationForm(ModelForm):
    class Meta:
        model=TeacherTable
        fields=['name','Department','email','phone_no','address']

class ReplyForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['reply']
class DepartmentForm(ModelForm):
    class Meta:
        model=DepartmentTable
        fields=['department']
