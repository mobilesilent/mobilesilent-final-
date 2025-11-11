from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


from mobilesilentapp.forms import ClassroomForm, DepartmentForm, ReplyForm, TeacherregistrationForm, TimingForm
from mobilesilentapp.models import *
# Create your views here.
class LoginPage(View):
    def get(self,request):
        return render(request,"administration/login.html")    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            obj = LoginTable.objects.get(username=username,password=password)
            request.session['user_id'] = obj.id

            # Handle based on user type
            if obj.user_type =='admin':
                return HttpResponse('''<script>alert("Wlcome back");window.location='/Admin_home'</script>''')
            elif obj.user_type =='teacher':
                return HttpResponse('''<script>alert("Wlcome back");window.location='/Teacher_Home'</script>''') 
            else:
                return HttpResponse('''<script>alert("User not found");window.location='/'</sript>''')
        except LoginTable.DoesNotExist:
            # Handle case where login details do not exist
            return HttpResponse('''<script>alert("Invalid username or password");window.location='/'</script>''')    


# ///////////////////////////////////// ADMIN //////////////////////////////////////////////////////

class ManageClassroom(View):
    def get(self,request):
        obj = ClassroomTable.objects.all()
        return render(request,"administration/manageClassroom.html", {'val':obj})

class Classroom(View):
    def get(self,request):
        return render(request,"administration/classroom.html")
    def post(self,request):
        form=ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ManageClassroom')

class ManageDepartment(View):
    def get(self,request):
        obj=DepartmentTable.objects.all()
        return render(request,'administration/managedepartment.html',{'department': obj})
    
class AddDepartment(View):
    def get(self,request):
        return render(request,'administration/department.html')
    def post(self,request):
        c=DepartmentForm(request.POST)
        if c.is_valid():
            r=c.save(commit=False)
            r.save()
            return HttpResponse('''<script>alert('entered successfully');window.location='Admin_home'</script>''')

class Complaints(View): 
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request,"administration/complaints.html", {'val': obj})
    
class Reply(View):
    def get(self,request,c_id):
        c=ComplaintTable.objects.get(id=c_id)
        return render(request, 'administration/replay.html')
    def post(self, request, c_id):
        c=ComplaintTable.objects.get(id=c_id)
        d = ReplyForm(request.POST, instance=c)
        if d.is_valid():
            d.save()
            return redirect('/Complaints')

class Feedback(View):
    def get(self,request):
        obj =FeedbackTable.objects.all()
        print(obj)
        return render(request,"administration/feedback.html",{'val':obj})
    
class TeacherRegister(View):
    def get(self,request):
        obj = DepartmentTable.objects.all()
        print(obj)
        return render(request,"administration/Register.html",{'dept':obj} )
    def post(self,request):
        c=TeacherregistrationForm(request.POST,request.FILES)
        if c.is_valid():
            r=c.save(commit=False)
            l=LoginTable.objects.create(username = request.POST.get('username'), password = request.POST.get('password'), user_type = 'teacher')
            r.login_id=l
            r.save()
            return HttpResponse('''<script>alert('Registration Successful');window.location='/'</script>''')




# //////////////////////////////////////////////////////////////////////////////////////



















   
class TimingView(View):
    def get(self, request):
        return render(request, "administration/timing.html")

    def post(self, request):
        form = TimingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<script>alert('Timing saved successfully');window.location='/Timing'</script>")
        else:
            return HttpResponse("<script>alert('Form is invalid');window.location='/Timing'</script>")

class Timetable(View):
    def get(self,request):
        return render(request,"administration/timetable.html")
class Teacherregistration(View):
    def get(self,request):
        return render(request,"administration/timetable.html") 
class Admin_home(View):
    def get(self,request):
        return render(request,"administration/admin_home.html")  
     
class ManageTimetable(View):
    def get(self,request):
        obj = Timing.objects.all()
        return render(request,"administration/manageTimetable.html")
class Select_class(View):
    def get(self,request):
        obj = Timing.objects.all()
        return render(request,"administration/select_class.html")
class View_timetable(View):
    def get(self,request):
       
        return render(request,"administration/View_timetable.html")
class Timetable_new(View):
    def get(self,request):
        obj = Timing.objects.all()
        return render(request,"administration/timetable_new.html")

class TeacherRegistaraion(View):
    def get(self,request):
        department = DepartmentTable.objects.all()
        return render(request,'teacherregistration.html',{'dept': department})
    def post(self,request):
        c=TeacherregistrationForm(request.POST,request.FILES)
        if c.is_valid():
            r=c.save(commit=False)
            l=LoginPage.objects.create(username = request.POST.get('username'), password = request.POST.get('password'), usertype = 'Pending')
            r.LOGIN_ID=l
            r.save()
            return HttpResponse('''<script>alert('Registration Successful');window.location='/'</script>''')
        

class ManageTeacher(View):
    def get(self,request):
        obj=TeacherTable.objects.all()
        department = DepartmentTable.objects.all()
        return render(request,'administration/manageteacher.html',{'val': obj, 'dept': department})
    def post(self,request):
        form=TeacherregistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'administration/manageteacher.html')
                
class DeleteDepartment(View):
    def get(self, request, id):
        obj = DepartmentTable.objects.get(id=id)     
        obj.delete()
        return redirect('ManageDepartment') 
    
class DeleteClassroom(View):
    def get(self, request, id):
        obj = ClassroomTable.objects.get(id=id)     
        obj.delete()
        return redirect('ManageClassroom') 
      
class TeacherView(View):
    def get(self, request):
        c = TeacherTable.objects.all()
        return render(request, 'administration/Teacher.html',{'c':c})
    
class AcceptTeacher(View):
    def get(self, request, id):
        c = TeacherTable.objects.get(id=id)
        c.login_id.user_type = 'teacher'
        c.login_id.save()
        return redirect('/teacher')
    
class RejectTeacher(View):
    def get(self, request, id):
        c = TeacherTable.objects.get(id=id)
        c.login_id.user_type = 'rejected'
        c.login_id.save()
        return redirect('/teacher')
    
class Teacher_Home(View):
     def get(self,request):
        return render(request,"teacher/teacher_home.html")

    
class View_Student(View):
    def get(self,request):
        obj=StudentTable.objects.all()
        return render(request,"teacher/view_student.html",{'obje':obj})

        ################################################################API###########################

        
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *  # Assuming you will be using the serializer for output
from rest_framework import status
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED
)

class LoginPageAPI(APIView):
    def post(self, request):
        print("####################")
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")
        print("$$$$$$$$$$$$$$",username)
        print("$$$$$$$$$$$$$$",password)
        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginTable.objects.filter(username=username, password=password).first()
        print("%%%%%%%%%%%%%%%%%%%%", t_user)

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        else:
            response_dict["message"] = "success"
            response_dict["login_id"] = t_user.id
            response_dict["user_type"] = t_user.user_type

            return Response(response_dict, status=HTTP_200_OK)




class StudentReg_api(APIView):
    def post(self, request):
        print("###################", request.data)

        user_serial = Student_Serializer(data=request.data)
        login_serial = Login_Serializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(user_type='STUDENT')

            # Assign the login profile to the UserTable and save the UserTable
            user_serial.save(LOGIN=login_profile)

            # Return the serialized user data in the response
            return Response(user_serial.data, status=status.HTTP_201_CREATED)

        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)
    

class AddReview(APIView):
    def post(self, request, id):
        print("📩 Incoming data:", request.data)

        try:
            # ✅ Get student by login id
            student = StudentTable.objects.get(LOGIN__id=id)
            print("✅ Found student:", student.name)
        except StudentTable.DoesNotExist:
            print("❌ Student not found for login id:", id)
            return Response({'error': 'Student not found'}, status=HTTP_400_BAD_REQUEST)

        # ✅ Deserialize the incoming feedback data
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            # ✅ Save feedback with foreign key
            serializer.save(user_id=student)
            print("✅ Feedback saved:", serializer.data)
            return Response({'message': 'success', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            print("❌ Serializer errors:", serializer.errors)
            return Response({'error': serializer.errors}, status=HTTP_400_BAD_REQUEST)



class AddComplaintAPI(APIView):
    def get(self, request, id):
        try:
            complaints = ComplaintTable.objects.filter(user_id__LOGIN__id=id)
            serializer = ComplaintSerializer(complaints, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("❌ Error fetching complaints:", e)
            return Response({"error": "Failed to fetch complaints"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        # ✅ Automatically get or create a student for the login id
        student, created = StudentTable.objects.get_or_create(
            LOGIN_id=id,
            defaults={"name": "AutoCreated User"}
        )

        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=student)
            print("✅ Complaint saved successfully:", serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("❌ Validation error:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimingAPI(APIView):
    def get(self, request):
        """
        Optional query param: ?day=Monday
        """
        try:
            day = request.GET.get('day', None)
            if day:
                timings = Timing.objects.filter(day__iexact=day)
            else:
                timings = Timing.objects.all()
            
            serializer = TimingSerializer(timings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("❌ Error fetching timings:", e)
            return Response({"error": "Failed to fetch timings"}, status=status.HTTP_400_BAD_REQUEST)