from django.contrib import admin

from mobilesilentapp.models import *

# Register your models here.
admin.site.register(LoginTable),
admin.site.register(StudentTable),
admin.site.register(ClassroomTable),
admin.site.register(Timing),
admin.site.register(FeedbackTable),
admin.site.register(ComplaintTable),
admin.site.register(TeacherTable)
admin.site.register(DepartmentTable)
admin.site.register(ClassTable)
admin.site.register(SubjectTable)
admin.site.register(Timetable1)