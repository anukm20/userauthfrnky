from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Products,UserDetails
from django.core.exceptions import ObjectDoesNotExist

def Home(req):
    products=Products.objects.all()
    return render(req,'index.html',{'products':products})

def Register(req):
    if req.method == 'POST':
        fname = req.POST.get("first_name", '')
        lname = req.POST.get("last_name", '')
        email = req.POST.get("email", '')
        username = req.POST.get("username", '')
        password = req.POST.get("password", '')
        cpassword = req.POST.get("cpassword", '')
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                print("Email already exists")
                return render(req, 'register.html', {'error': 'Email already exists'})
            elif User.objects.filter(username=username).exists():
                print("Username already exists")
                return render(req, 'register.html', {'error': 'Username already exists'})
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password)
                user.save()
                return redirect("Login")
        else:
            print('Password not matching')
            return render(req, 'register.html', {'error': 'Passwords do not match'})
    return render(req, 'register.html')

def login(req):
    if req.method=='POST':
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(req,user)
          print(user)
          req.session['user']=str(user)
          return redirect('profile',id=user.id)
        else:
            print("invalid")
            return redirect('Login')
    return render(req,'login.html')

def logout(req):
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('home')


def  Profile(req,id):
    user_details = UserDetails.objects.filter(user=id)
    use = User.objects.get(id=id)
    if req.method=="POST":
        image=req.FILES['image']
        phone=req.POST.get('phone','')
        destination=req.POST.get('destination','')
        experience=req.POST.get('experience','')

        userdetail=UserDetails(user=use,image=image,phone=phone,destination=destination,experience=experience)
        userdetail.save()
    return render(req,'profile.html',{"user_details":user_details})