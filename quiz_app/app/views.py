from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "app/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        if User.objects.filter(email=email):
            messages.error(request, "Email already Exist!")
            return redirect('home')


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account is created Sucessfully.")

        return redirect('signin')

    return render(request, "app/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "app/quiz.html", {'fname': fname})
        
        else:
            messages.error(request, "Wrongh Credentials")
            return redirect('home')

    return render(request, "app/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def quiz(request):
    if request.method == "POST":
        score = request.POST['score']
        myuser = User.objects.create_user(score)
        myuser.save()
        

    return render(request, "app/quiz.html")