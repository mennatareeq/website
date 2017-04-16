from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from users.forms import RegistrationForm
from django.contrib.auth.models import User
from users.models import UserAccount

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
            return HttpResponseRedirect('/profile/')
        else:
            return render(request , 'register.html' , {'form': form})
    else:
        '''user is'nt submitting the form, show them a blank registration form'''
        form = RegistrationForm()
        return render(request,'register.html', {'form' : form})

