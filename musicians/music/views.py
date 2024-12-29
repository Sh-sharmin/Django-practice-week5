from django.shortcuts import render, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm,SignupForm,ChangeUserdata
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,logout,login,update_session_auth_hash


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                messages.success(request,'Account created Successfully')
                signup_form.save()
                return redirect('musician_list')  
        else:
            signup_form = SignupForm()
        return render(request, 'signup.html', {'form': signup_form})
    else:
        return redirect('musician_list')


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
                    return redirect('musician_list')
        else:
            form =AuthenticationForm()
    else:
        return redirect('profile')
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'Logged out Successfully')
    return redirect('musician_list')


# List View
def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians})

#Edit Musician
def musician_edit(request, musician_id):
    musician = Musician.objects.get(pk=musician_id)
    form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    return render(request, 'musician_form.html', {'form': form})

# Edit Album
def album_edit(request, album_id):
    album = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    return render(request, 'album.html', {'form': form})

# Delete
def delete_item(request, item_id):
    musician = Musician.objects.get(pk=item_id)
    musician.delete()
    return redirect('musician_list')

