from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from App_Login.models import UserProfile

# Create your views here.




def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/signup.html', context={'title': 'SignUp Form', 'form':form})



def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # return render(request, 'App_Stream/comments.html', context={})
                return HttpResponseRedirect(reverse('App_Stream:home'))
                # return HttpResponse('<h3>Logged in!! </h3>')

    return render(request, 'App_Login/login.html', context={'title': 'Login', 'form':form})




@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Stream:home'))
    # return HttpResponse('<h3>Logged Out!!</h3>')



@login_required
def profile(request):
    form = EditProfile()
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse())
    return render(request, 'App_Login/user.html', context={'title':'User', 'form':form})

























#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
