from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from login.models import xeroxdetails


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,"a2.html")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'a.html')

def xerox(request):
    det=xeroxdetails()
    det.name='Name'
    det.branch='Branch'
    det.hostelname='Hostel name'
    det.roomno='Room no.'
    det.contectno='WhatsApp no.'
    det.image='Image'

    return render(request,'orignal.html',{'det': det})

def store(request):
    name = request.POST['name']
    branch = request.POST['branch']
    hostelname = request.POST['hostelname']
    roomno = request.POST['roomno']
    contectno = request.POST['contectno']
    
    store=xeroxdetails(name=name,branch=branch,hostelname=hostelname,roomno=roomno,contectno=contectno)
    store.save();
    return render(request,'thank.html')



