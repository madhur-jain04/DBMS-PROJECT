from datetime import date, datetime

from django.http import HttpResponse
from django import forms
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
import mysql.connector
from LateEntry.credentialManager import CredentialManager as cm

connection = mysql.connector.connect(user=cm.user, password=cm.password, host=cm.host, database=cm.database,
                                     autocommit=True)

import pytz

# get the standard UTC time
UTC = pytz.utc

# it will get the time zone
# of the specified location
IST = pytz.timezone('Asia/Kolkata')

class InsertForm(forms.Form):
    guardID = forms.IntegerField()
    rollNumber = forms.IntegerField()
    reason = forms.CharField(max_length=100, required=False)


# Create your views here.
class InsertView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.email == "Guard":

            return render(request, "insert.html")
        else:
            return redirect("login")

    def post(self, request):
        user = request.user
        if user.is_authenticated and user.email == "Guard":
            form = InsertForm(request.POST)
            if form.is_valid():
                guardID = form.cleaned_data['guardID']
                rollNumber = form.cleaned_data['rollNumber']
                reason = form.cleaned_data['reason']
                currentDate = date.today().strftime("%Y-%m-%d")
                currentTime = datetime.now().strftime("%H:%M:%S")

                if int(currentTime[0:2]) < 2:
                    penalty = 2
                elif int(currentTime[0:2]) < 6:
                    penalty = 3

                elif int(currentTime[0:2]) < 23:
                    penalty = 1

                print(guardID, rollNumber, reason)
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO entry_info(roll_no,g_id,reason,entry_time,entry_date,penalty_type) VALUES(%s,%s,%s,%s,%s,%s)",
                        (rollNumber, guardID, reason, currentTime, currentDate,penalty))
            else:
                return HttpResponse(form.errors)

            return redirect("insert")

# Create your views here.
