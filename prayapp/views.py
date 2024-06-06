from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from prayapp.models import*
import json
from django.utils import timezone

# Create your views here.


def home(request):    
        return render(request, "index.html")
    
def login(request):
        if request.method == "POST":
                uname = request.POST['uname']
                pwd = request.POST['pwd']
                print(uname, pwd)
                l=Login.objects.all()
                q=l.filter(username=uname, password=pwd)
               
                if q.exists():
                         user =l.get(username=uname,password=pwd)
                         uid = User.objects.get(login_id=user.pk)
                         request.session['uid'] =uid.pk
                         request.session['login_id'] =user.pk
                         print(request.session['uid'])
                         return redirect('userhome')
                else:
                        messages.error(request,"Invalid username or password")
                        # return HttpResponse("<script> alert('User doesnot exist'); window.location='/login' ;  </script>")
                        return redirect('login')
        else:
                return render(request, "login.html")







def registration(request):
        
        if request.method == "POST":
                name = request.POST.get("name")
                place = request.POST.get("place")
                age = request.POST.get("age")
                gender = request.POST.get("gender")
                number = request.POST.get("number")
                email = request.POST.get("email")
                username = request.POST.get("username")
                pwd = request.POST.get("password")
                photo = request.FILES.get("photo",None)

                print(name, age, gender, number, email,username, pwd, photo)
                


                logobj = Login(username=username, password=pwd)
                logobj.save()
                userid =logobj.pk
                reg = User(name=name,place=place,age=age,gender=gender,number=number,email=email,login_id=userid,photo=photo)
                reg.save()

                if reg:
                        return redirect('login')
                else:
                        return HttpResponse("<script>alert('Registration Failure try agian!!');window.location='/register'</script>")      

        return render(request, "registration.html")


def userhome(request):
        print("Welcome")
        if request.method == "POST":   
                      data = json.loads(request.body)
                      print(data)
                      print(data.items())
                      i = 1
                      lid = request.session['login_id'] 
                      uid = User.objects.get(login_id=lid)
                      user_id = uid.pk
                     
                     
                                        
                      for prayer,times in data.items():
                        #    p = Prayer.objects.get(name = prayer) #p = Prayer.objects.get(name = prayer)
                           p = Prayer.objects.get(name = prayer)
                           print(p)
                           print(prayer,times)
                           q = Prayer_marking(user=uid,prayer=p,date=timezone.now().date(), ontime=times['ontime'],aftertime=times['late'],with_imam=times['withImam'],missed=times['missed'])
                           print (q) 
                           q.save()
                        # print (fajr,fajr_imam,dhuhr,dhuhr_imam,asr,asr_imam,maghrib, maghrib_imam,isha,isha_imam)

        return render(request, "userhome.html")
                






     