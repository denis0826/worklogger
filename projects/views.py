from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django_ajax.decorators import ajax

from .models import Project, Log


def index(request):
    if request.user.is_authenticated():

        if request.method == "POST":
            date = request.POST['date']
            time = request.POST['time']
            remarks = request.POST['remarks']
            project_id = request.POST['project_id']
            created = timezone.now()

            log = Log.objects.create(date=date, time=time, remarks=remarks, created=created, project_id=project_id)
            log.save()

            return HttpResponseRedirect('/')

        queryset = Project.objects.all()

        context = {
            "project_list": queryset,
            "title": "Worklogger",
        }

        return render(request, 'index.html', context)

    else:
        return redirect('login')


def my_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return None

    else:
        return render(request, 'login.html', {})


def my_logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return redirect('login')

@ajax
def show_date(request):
    date = request.GET['date']
    new_query = Log.objects.all().filter(date=date)

    context = {
        'project_log': new_query
    }
    return render(request, 'date.html', context)
