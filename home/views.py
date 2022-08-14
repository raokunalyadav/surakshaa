from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def sendsms(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        numbers = request.POST['numbers']
        numlist = numbers.split('\r\n')
        finalnums = ",".join(numlist)

        namelist = name.split(' ')
        finalname = "%20".join(namelist)

        url = "https://www.fast2sms.com/dev/bulkV2"
        payload = f"message={finalname}%20is%20in%20trouble%20Her%20exact%20current%20location%20with%20latitude%20and%20longitude%20is%20{location}%20Type%20this%20in%20GMaps&language=english&route=q&numbers={finalnums}"
        headers = {
            'authorization': "o6KMfVuycU7mFZrHNjqE13A0WRXlvwdT8PGOkBzsxJ5Dht9Lb2N7E4G0awp8oPbnfxyTrtuOkDFvIqCU",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        if 'sent' in response.text:
            messages.success(request, "Alert sent to your closed-ones.")
        else:
            messages.error(request, "Some error occured.")

        print(response.text)


    return render(request, 'home/home.html')
