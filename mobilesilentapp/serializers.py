from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class TimingSerializer(ModelSerializer):
    class Meta:
        model = Timing
        fields = ['id', 'day', 'start', 'to', 'subject']


class Login_Serializer(ModelSerializer):
    class Meta:
        model = LoginTable
        fields = '__all__'

class Student_Serializer(ModelSerializer):
    class Meta:
        model = StudentTable
        fields = '__all__'

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = FeedbackTable
        fields = '__all__'


class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = '__all__'

class TimetableSerializer(serializers.ModelSerializer):
    subject1 = serializers.CharField(source='slot_9_10.Subject')
    subject2 = serializers.CharField(source='slot_10_11.Subject')
    subject3 = serializers.CharField(source='slot_11_12.Subject')
    subject4 = serializers.CharField(source='slot_12_1.Subject')
    subject5 = serializers.CharField(source='slot_2_3.Subject')
    class Meta:
        model = Timetable1
        fields = ['day', 'subject1','subject2', 'subject3', 'subject4', 'subject5'] 

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassTable
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentTable
        fields='__all__'
