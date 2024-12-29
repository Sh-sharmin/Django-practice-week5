from django.shortcuts import render,redirect
from .forms import SignupForm,ChangeUserdata
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,logout,login,update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                messages.success(request,'Account created Successfully')
                signup_form.save()
                return redirect('signup')  
        else:
            signup_form = SignupForm()
        return render(request, 'signup.html', {'form': signup_form})
    else:
        return redirect('homepage')


def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass) #checking if user is in database
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return redirect('profile')
        else:
            form =AuthenticationForm()
    else:
        return redirect('profile')
    return render(request,'login.html',{'form':form})

@login_required
def profile(request):
    return render(request,'profile.html')
@login_required
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user =request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')

@login_required
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user =request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'Logged out Successfully')
    return redirect('homepage')