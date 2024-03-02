from django.shortcuts import render,redirect
from justdial.models import Hostel, Subscribe
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate, login as auth_loging
from django.contrib.auth.decorators import login_required


# Create your views here.
def Singup(request):
    context ={}

    if request.method == "GET":
        return render(request,'Singup.html')
    else:
        n= request.POST['name']
        p= request.POST['password']
        cp= request.POST['cp']

      
    if n == '' or p == '' or cp == '':
        context['errmsg'] = "fields can not be empty"
        return  render(request,'Singup.html',context)
    elif p!= cp:
        context['errmsg'] = "password do not match the confirm password"
        return  render(request,'Singup.html',context)
    elif len(p)<8 or len(p)>15:
        context['errmsg'] = "length of the password should be grater than 8 and less than 15"
        return  render(request,'Singup.html',context)
    else:
        try:
            u = User.objects.create(username= n,password=p)
            u.set_password(p)
            u.save()
            context['success']="Registered successfully !!"
            return redirect('login')
        except Exception as e:
            context['errmsg'] ="already registered please login!!"
            return render(request,'Singup.html',context)


def login(request):
    if request.method=="GET":
        return render(request,"Loging.html")     
    else:
        n = request.POST['name']
        p = request.POST['password'] 
        print(n)
        print(p)
        u = authenticate(username=n,password=p) 
        print(u)
        if u is not None:
            auth_loging(request, u)
            return redirect("Home")
        else:
            context = {}       
            context['errmsg']= "invalid username or password "
            return render(request,"Loging.html",context)

def user_logout(request):
    logout(request)
    return redirect("Home")

def firsthome(request):
    return render(request,'firsthome.html')

def home(request):
    index= Hostel.objects.all()
    context={}
    context['hostel']=index
    return render(request, 'homepage.html',context)

def pune(request):
    h = Hostel.objects.filter(city="pune")
    context = {}
    context ['hostel'] = h
    return render(request, 'pune.html', context)
 
def index(request):
    h = Hostel.objects.filter(city="Delhi")
    context = {}
    context ['hostel'] = h
    return render(request, 'index.html', context)

def Chennai(request):
    h = Hostel.objects.filter(city="Chennai")
    context = {}
    context ['hostel'] = h
    return render(request, 'Chennai.html', context)
def Hyderabad(request):
    h = Hostel.objects.filter(city="Hyderabad")
    context = {}
    context ['hostel'] = h
    return render(request, 'Hyderabad.html', context)
@login_required(login_url='login')
def detil(request,pid):
    index = Hostel.objects.get(id=pid)
    context = {}    
    context['hostel']=index
    print(context['hostel'])
    return render(request, 'showDatils.html',context)


def about(request):
    return render(request,'About.html')
def faq(request):
    return render(request,'faq.html')
def subscribe(request):
   email = request.POST['Semail']
   
   e = Subscribe(email=email)
   e.save()
   return redirect('Home')