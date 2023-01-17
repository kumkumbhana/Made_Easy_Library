from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Contact

#below import is for sending emails.
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage




def index(request):
    return render(request,'Authenticate/index.html')

def home(request):
    return render(request,'Authenticate/home.html')

def fiction(request):
    return render(request,'Authenticate/fiction.html')

def nonfiction(request):
    return render(request,'Authenticate/nonfiction.html')

def novel(request):
    return render(request,'Authenticate/novel.html')

def story(request):
    return render(request,'Authenticate/story.html')

def programming(request):
    return render(request,'Authenticate/programming.html')

def engineering(request):
    return render(request,'Authenticate/engineering.html')



def about(request):
    return render(request,'Authenticate/about.html')

def contact(request):
    if request.method=="POST":
        fname= request.POST.get("name")
        femail= request.POST.get("email")
        phone= request.POST.get("phone")
        desc= request.POST.get("desc")
        query=Contact(name=fname,email=femail,phoneNumber=phone,description=desc)
        query.save()

        # emails sending starts from here
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        email_message=mail.EmailMessage(f'Email from {fname}',f'UserEmail:{femail}\nUserPhoneNumber : {phone}\n\n\n QUERY : {desc}',from_email,['prachandharshal@gmail.com','madeeasy63@gmail.com'],connection=connection)
        connection.send_messages([email_message])
        connection.close()

        messages.info(request,"Thanks For Reaching Us! We Will Get Back You Soon... ")
        return redirect('/contact')
    return render(request,'Authenticate/contact.html')


def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")

        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfull")
            return redirect('/home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')

    return render(request,'Authenticate/login.html')

def handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        # print(uname,email,password,confirmpassword)
        if password != confirmpassword:
            messages.warning(request,"Password Is Incorrect")
            return redirect('/signup')

        try:
            if User.objects.get(username=uname):
                messages.info(request, "UserName Is Taken")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, "Email Is Taken")
                return redirect('/signup')
        except:
            pass
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request, "Sign Up Is Successful, Please Log In")
        return redirect('/login')

    return render(request,'Authenticate/signup.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logged Out Successfully")
    return redirect('/login')

def feedback(request):
    return render(request,'Authenticate/feedback.html')

def addbook(request):
    return render(request,'Authenticate/addbook.html')