from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from justdial import views

urlpatterns = [
   path('',views.firsthome,name="firsthome"),
   path('Home',views.home, name='Home'),
   path('Singup',views.Singup, name='Singup'),
   path('login',views.login, name="login"),
   path('user_logout',views.user_logout, name='user_logout'),
   path('index',views.index, name='index'),
   path('pune',views.pune, name='pune'),
   path('Chennai',views.Chennai, name='Chennai'),
   path('Hyderabad',views.Hyderabad, name='Hyderabad'),
   path('detil<pid>', views.detil, name='detil'),
   path("about",views.about, name='about'),
   path('faq',views.faq, name="faq"), 
   path('subscribe',views.subscribe, name='subscribe'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)