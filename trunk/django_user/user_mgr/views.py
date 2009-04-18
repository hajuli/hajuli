# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

"""
def sign_up(request):
    form = UserCreationForm()
    # if form was submitted, bind form instance.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            user = form.save(commit=True)
            # user must be active for login to work
            user.is_active = True
            # user.put()
            return HttpResponseRedirect('/user_mgr/sign_in/')
    return render_to_response('user_mgr/sign_up.html', {'form': form})

def sign_in(request):
    from django.http import HttpResponse
    return  HttpResponse("xxx")

"""