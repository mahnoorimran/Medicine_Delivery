from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import *
from .models import *
from .forms import CustomUserCreationForm,ProfileForm, CustForm ,UpdateCustForm,UpCustomUserCreationForm

# Create your views here.
def loginPage(request):
    page='login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'Username dosenot exit')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User successfully logout')
    return redirect('login')


def registerUser(request):
    page='register'
    form=CustomUserCreationForm()
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            Customer.objects.create(
                    user = user,
                    name = user.username,
                    email = user.email
                )
            messages.success(request, 'User account was created successfully!!')
            # login(request,user)
            return redirect('login')
        else:
            messages.success(request, 'Error occurred during registration')
    context={'page':page,'form':form}

    return render(request,'users/login_register.html',context)



def profile(request):
    profiles=Profile.objects.all()
    context={
        'profiles':profiles
    }
    return render(request,'users/profile.html',context)

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    context={
        'profile':profile
    }
    return render(request,'users/user-profile.html',context)


@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    context={
        'profile':profile,
    }
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={
        'form':form,
    }
    return render(request,'users/profile_form.html',context)

def custpanel(request):
    if request.user.is_authenticated:
        # customer = request.user
        orders=OrderItem.objects.filter(order__customer=request.user.customer).count()
    context={ 'orders':orders}
    return render(request,'users/dashboard.html',context)


        
