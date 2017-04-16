from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from users.forms import RegistrationForm,LogInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from users.models import UserAccount
from django.core.urlresolvers import reverse


def UserRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            user.save()
            user_account = UserAccount(user=user,
                                       username=form.cleaned_data['username'],
                                       email=form.cleaned_data['email'],
                                       password=form.cleaned_data['password'])
            user_account.save()
            return HttpResponseRedirect('photos:index')
        else:
            return render(request , 'register.html' , {'form': form})
    else:
        '''user is'nt submitting the form, show them a blank registration form'''
        form = RegistrationForm()
        return render(request,'register.html', {'form' : form})

def loginrequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('photos:index')
    if request.method=="POST":
        form=LogInForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('photos:index'))
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request,'login.html',{'form':form})
    else:
        '''user is not submitting form, show the login form'''
        form = LogInForm()
        context={'form':form}
        return render(request,'login.html',context)
