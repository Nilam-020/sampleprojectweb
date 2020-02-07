from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print("username taken")
                messages.info(request, 'Username taken')
            elif User.objects.filter(email==email).exists():
                    # print("email already taken")
                    messages.info(request, 'Email taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            # print('password not matched.')
            messages.info(request, 'Password wrong')
            return redirect('/')
    else:
        return render (request,'register.html')


def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')