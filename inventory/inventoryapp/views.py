from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username','')
        password = request.POST['password']
        oUser_list = User.objects.all()
        for list in oUser_list:
            if (list.username == user_name and list.password == password):
                return redirect('/dashboard/')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username','')
        email = request.POST['email']
        password = request.POST['password']
        oUser = User(username=user_name, email=email, password=password)
        oUser.save()
        return redirect('/')
    return render(request, "register.html")

# def newaccount(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username','')
#         email = request.POST['email']
#         password = request.POST['password']
#         print(user_name)
#         user = User(username=user_name, email="email@gmail.com", password="123456")
#         user.save()
#         # return render(request, 'registration/success.html')
#     return render(request, 'registration/register.html')

def dashboard(request):
    return render(request,"dashboard.html")