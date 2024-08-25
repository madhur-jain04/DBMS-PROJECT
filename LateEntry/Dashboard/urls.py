from .views import *
from django.urls import path

urlpatterns = [
    path('warden', WardenDashBoardView.as_view(), name='warden'),
    path('guard', GuardDashBoardView.as_view(), name='guard'),
    path('student', StudentDashBoardView.as_view(), name='student'),

]
