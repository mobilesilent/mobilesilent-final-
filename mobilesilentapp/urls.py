
from django import views
from django.contrib import admin
from django.urls import include, path

from mobilesilentapp.views import *

urlpatterns = [

    path('',LoginPage.as_view(),name="LoginPage"),

    # /////////////////////////////// ADMIN //////////////////////////////////////////////////////////
    path('ManageClassroom',ManageClassroom.as_view(),name="ManageClassroom"),
    path('classroom',Classroom.as_view(),name="Classroom"),
    path('ManageDepartment',ManageDepartment.as_view(),name="ManageDepartment"),
    path('AddDepartment',AddDepartment.as_view(),name="AddDepartment"),
    path('Complaints',Complaints.as_view(),name="Complaints"),
    path('Reply/<int:c_id>',Reply.as_view(),name="Reply"),
    path('Feedback',Feedback.as_view(),name="Feedback"),
    path('teacher',TeacherView.as_view(),name="teacher"),
    path('Timing', TimingView.as_view(), name='Timing'),
    path('acceptteacher/<int:id>', AcceptTeacher.as_view()),
    path('rejectteacher/<int:id>', RejectTeacher.as_view()),
    path("manage_timetable",manage_timetable.as_view(), name="manage_timetable"),
    path("add_timetable_action",add_timetable_action.as_view(), name="add_timetable_action"),
    path("select_class1/",select_class_staff.as_view(), name="select_class_staff"),
    path("view_timetable",view_timetable1.as_view(), name="view_timetable"),
    
# ////////////////////////////////////////////////////////////////////////////////////////////////




    # path('Timing',Timing.as_view(),name="Timing"),
    path('TeacherRegister',TeacherRegister.as_view(),name="TeacherRegister"),
    path('Timetable',Timetable.as_view(),name="Timetable"),
    path('Teacherregistration',Teacherregistration.as_view(),name="Teacherregistration"),
    path('Admin_home',Admin_home.as_view(),name="Admin_home"),
    path('Select_class',Select_class.as_view(),name=" "),
    path('Timetable_new',Timetable_new.as_view(),name="Timetable_new"),
    path('ManageTeacher',ManageTeacher.as_view(),name="ManageTeacher"),
    path('DeleteDepartment/<int:id>',DeleteDepartment.as_view(),name="DeleteDepartment"),
    path('DeleteClassroom/<int:id>',DeleteClassroom.as_view(),name="DeleteClassroom"),
    path('Teacher_Home',Teacher_Home.as_view(),name="Teacher_Home"),
    path('Viewstudent',View_Student.as_view(),name="View_Student"),
    path("view_timtable_action", view_timtable_action.as_view(), name="view_timtable_action"),
    path("manage_class",manage_class.as_view(), name="manage_class"),
    path("add_class",add_class.as_view(), name="add_class"),
    path("add_class_post",add_class_post.as_view(), name="add_class_post"),
    path("delete_class/<int:class_id>",delete_class.as_view(), name="delete_class"),

    ##########################api########################3

    path('login', LoginPageAPI.as_view(), name='login'),
    path('studentreg_api/', StudentReg_api.as_view(), name='studentreg_api'),
    path('feedback_api/<int:id>', AddReview.as_view(), name='feedback_api'),
    path('complaint_api/<int:id>', AddComplaintAPI.as_view(), name='complaint_api'),
    path('timings_api/', TimingAPI.as_view(), name='timings_api'),
    path('ViewTimeTable/<int:lid>', ViewTimeTable.as_view(), name="ViewTimeTable"),
    path('ViewClassrooms', ViewClassRooms.as_view(), name="ViewClassrooms"),
    path('ViewDepartmentApi',ViewDepartmentApi.as_view(),name="ViewDepartmentApi"),

]
