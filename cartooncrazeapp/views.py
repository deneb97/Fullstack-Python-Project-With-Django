from django.shortcuts import render
from.models import Feedback
from datetime import datetime
from django.contrib.auth.models import User




# Create your views here.

def home(request):
        if request.method == "POST":
            print("POST DATA:", request.POST)

            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone_number=request.POST.get('phone_number')
            feedback=request.POST.get('feedback')
            
            
            user = User.objects.create_user(username=name, email=email, password=password)

            home=Feedback(name=name,email=email,password=password,address=address,phone_number=phone_number,
                            feedback=feedback,date=datetime.today())
            home.save()
           
            
              
        return render(request, 'index.html')


        