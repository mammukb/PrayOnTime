from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from prayapp.models import*
from django.contrib.auth import authenticate, login as auth_login

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
                count = q.count()
                


                if count == 1:
                         user =q.first()
                         request.session['username'] =user.username
                        #  return HttpResponse("<script> alert('Login Suceess'); window.location='/userhome' ;  </script>")
                         return redirect('userhome')
                else:
                        messages.error(request,"Invalid username or password")
                        return HttpResponse("<script> alert('User doesnot exist'); window.location='/login' ;  </script>")
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
        return render(request, "userhome.html")