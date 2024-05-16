from django.contrib import messages, auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import UserProfile,loginTable

# Create your views here.
#
#def Register_user(request):
#
#   if request.method=='POST':
#
#        username=request.POST.get('username')
#        first_name=request.POST.get('first_name')
#        last_name=request.POST.get('last_name')
#       email=request.POST.get('email')
#        password=request.POST.get('password')
#        cpassword=request.POST.get('password1')

#       if password==cpassword:
#         if User.objects.filter(username=username).exists():
#                messages.info(request,'this username already exist')
#                return redirect('register')
#            elif User.objects.filter(email=email).exists():
#               messages.info(request,"This mail already taken")
#               return redirect('register')
#
#           else:
#                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
#                user.save()
#
#            return redirect('login')
#        else:
#            messages.info(request,'This password not matching')
#           return redirect('register')


#   return render(request,'register.html')


#def  loginUser(request):
#    if request.method=='POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user=auth.authenticate(username=username,password=password)
#
#       if user is not None:
#            auth.login(request,user)
#           return redirect('home')
#        else:
#           messages.info(request,'please provide correct details')
#            return redirect('login')
#    return render(request,'login.html')


#def logOut(request):
#    auth.logout(request)
#    return redirect('login')

#def HomePage(request):

#    return render(request,'home.html')

def userRegistration(request):

    login_table=loginTable()
    userprofile=UserProfile()

    if request.method=='POST':

        userprofile.username=request.POST['username']
        userprofile.password = request.POST['password']
        userprofile.password2 = request.POST['password1']

        login_table.username=request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password1']
        login_table.type='user'

        if request.POST['password']==request.POST['password1']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration success')
            return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    return render(request,'register.html')


def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=loginTable.objects.filter(username=username,password=password,type='user').exists()
        try:

            if user is not None:

                user_details=loginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type=='user':
                    request.session['username']=user_name
                    return redirect('user_view')
                elif type=='admin':
                    request.session['username']=user_name
                    return redirect('admin_view')
            else:
                messages.error(request,'invalid username or password')

        except:
            messages.error(request,'invalid role')
    return render(request,'login.html')


def admin_view(request):
    user_name=request.session['username']

    return render(request,'admin_view.html',{'user_name':user_name})

def user_view(request):
    user_name=request.session['username']

    return render(request,'user_view.html',{'user_name':user_name})



def logout_view(request):
    logout(request)
    return redirect('login')


















