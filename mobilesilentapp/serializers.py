from rest_framework.serializers import ModelSerializer
from .models import *

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