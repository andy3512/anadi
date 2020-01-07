from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('register')
        else:
            user= User.objects.create_user(username=username, password=password)
            user.save();
            print('user created')
            return redirect('/')

    else:
        return render(request,'a.html')


def logout(request):
    auth.logout(request)
    return redirect('/')