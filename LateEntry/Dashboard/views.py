from django.shortcuts import render
from django.views import View


# Create your views here.
class GuardDashBoardView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.email == "Guard":
            return render(request, 'guard_dashboard.html')


class StudentDashBoardView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.email == "Student":
         return render(request, 'student.html')


class WardenDashBoardView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.email == "Warden":
            return render(request, 'warden_dashboard.html')
