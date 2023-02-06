from django.shortcuts import render,redirect
from . forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile,Stream, Classes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    streams = Stream.objects.all()
    return render(request,'index.html', {"streams": streams})

def classes(request, id):
    classes = Classes.objects.filter(id = id)
    return render(request,'one.html', {"classes": classes})

def students(request, id):
    students = Profile.objects.filter(classes = id, role = "student")
    return render(request,'students.html', {"students": students})


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,email=email, password=raw_password)
            profile = Profile(user=user)
            profile.save()
            user.is_active = True

            login(request,user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'reg.html', {'form': form})
    
@login_required(login_url='/auth/login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    return render(request,'profile/profile.html',{})


@login_required(login_url='/auth/login')
def profiles(request,id):
    profile = Profile.objects.get(user_id=id)
    return render(request,'profile/profiles.html',{"profile":profile})

def search_results(request):

    if 'user' in request.GET or request.GET['user']:
        search_item = request.GET.get('user')
        searched_users = User.objects.filter(username=search_item)
        print(searched_users)
        message = f"{search_item}"
        return render(request, 'search.html',{"message":message,"users": searched_users})
    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})
