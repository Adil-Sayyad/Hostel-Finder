from django.shortcuts import redirect
from django.urls import reverse

def login_required(view_func):
    def wrapper(request):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        return view_func(request,'showDatils.html')
    return wrapper