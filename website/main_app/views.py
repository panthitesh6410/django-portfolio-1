from django.shortcuts import render
from . models import enquiry

# Create your views here.

def index(request):
    if request.method =='POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_message = request.POST['message']
        e = enquiry(name=user_name, email=user_email, message=user_message)
        e.save()
        message = {'message':'Your Message has been sent successfully '}
        return render(request,'main_app/index.html', {'message':message})
    else:
        return render(request,'main_app/index.html')