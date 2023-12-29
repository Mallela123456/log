from django.shortcuts import render,redirect,HttpResponse
from .models import Employee


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if password == conpassword:
            user = Employee(name = username,email = email,password = password,conpassword = conpassword)
            user.save()
            return redirect(login)
        else:
            return HttpResponse('password and confirmpassword not matching')
        
        
            
    return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password_1 = request.POST['password']
        user_data = Employee.objects.all()
        user_present = None
        for user in user_data:
            if (user_name,password_1) == (user.name,user.password):
                user_present = user.name
        if user_present is not None:
            return redirect(home)
        else:
            return HttpResponse("invalid creditials")
        
        
    return render(request,'login.html')
def home(request):
    if request.method == 'POST':
        return redirect(login)
    return render(request,'home.html')