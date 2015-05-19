from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from skillstudents.models import SkillsStudents
from django.forms import ModelForm
from django.views.generic import CreateView
from django.views.generic import ListView


# Create your views here.

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    print username
    print password
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    #return render_to_response('loggedin.html', {'full_name':request.user.username})
    return render_to_response('saestudents_form.html', {'full_name':request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def invalid_login(request):
    auth.logout(request)
    return render_to_response('invalid_logout.html')

class CreateView(CreateView):
    model = SkillsStudents
    
    def get_success_url(self):
        return reverse('student_list')

class ListContactView(ListView):
    model = SkillsStudents
    template_name = 'student_list.html'
    
    
class ServerForm(ModelForm):
    class Meta:
        model = SkillsStudents

def studentadded(request):
    print "Entrando a studentadded"
    if (request.POST):
        print "Es un POST"
        form = ServerForm(request.POST or None)
        if form.is_valid():
                print "La forma es valida"
                form.save()
                return HttpResponseRedirect('/accounts/loggedin')
    else:
        return render_to_response('skillsstudents_form.html', {'full_name':request.user.username})