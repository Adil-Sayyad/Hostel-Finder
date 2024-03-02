from django.db import models

# Create your models here.
class Hostel(models.Model):
    AW=(('Attached Washroom','Attached Washroom'),('Not Attached Washroom','Not Attached Washroom'))
    AC=(('Spacious Cupboard','Spacious Cupboard'),('Not Spacious Cupboard','Not Spacious Cupboard'))
    Hname = models.CharField(max_length=100)
    gen = models.CharField(max_length=20)
    loc = models.CharField(max_length=100)
    addr = models.CharField(max_length=255)
    desc = models.TextField()
    num = models.CharField(max_length=20)
    rent = models.CharField(max_length=20)
    img1 = models.ImageField(upload_to='static/image')
    img2 = models.ImageField(upload_to='static/image')
    img3 = models.ImageField(upload_to='static/image')
    img4 = models.ImageField(upload_to='static/image')
    rbad1 = models.CharField(max_length=100, default=0) 
    rbad2 = models.CharField(max_length=100, default=0) 
    rbad3 = models.CharField(max_length=100, default=0) 
    rbad4 = models.CharField(max_length=100, default=0) 
    city = models.CharField(max_length=100, default='pune')
    am = models.CharField(max_length=100,verbose_name = 'Amenities',choices=AW, default='Attached Washroom')
    ac = models.CharField(max_length=100,verbose_name = 'Amenities',choices=AC, default='Spacious Cupboard')
    ser1 = models.CharField(max_length=100, default='Spacious Refrigerator') 
    ser2 = models.CharField(max_length=100, default='Washing Machine') 
    ser3 = models.CharField(max_length=100, default='Hot Water Supply') 
    
    
class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
    
    