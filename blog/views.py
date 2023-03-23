from django.shortcuts import render
from .models import *


def index(request):
    teachers = Teacher.objects.order_by('-date')[:3]
    circles = Circle.objects.order_by('-date')[:4]
    news = New.objects.order_by('-date')[:3]
    info = Info.objects.order_by('-date')[:1]
    meetings = Meeting.objects.order_by('-date')[:5]
    instagram = Instagram.objects.order_by('-date')[:4]
    events = Event.objects.order_by('-date')[:3]
    content = {'teachers':teachers, 'circles':circles, 'news':news, 'infos':info, 'instagrams':instagram, 'meetings': meetings, 'events':events}
    return render(request, 'index.html', content)

def circles(request):
    circles = Circle.objects.all()
    return render(request, 'circles.html', {'circles':circles})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers':teachers})

def meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings.html', {'meetings':meetings})

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events':events})

def event(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'event.html', {'event':event})

def setificat(request):
    sertificats = Teacher.objects.order_by('sertificat')
    return render(request, 'sertificat.html', {'teachers':sertificats})

def meeting(request,id):
    meeting = Meeting.objects.get(id=id)
    return render(request, 'meeting.html', {'meeting':meeting})

def news(request):
    news = New.objects.all()
    return render(request, 'news.html', {'news':news})

def teacher(request, id):
    if Teacher.objects.get(id=id):
        teacher = Teacher.objects.get(id=id)
        return render(request, 'teacher.html', {'teacher':teacher})
    else:
        return render(request, 'notfount.html')

def circle(request, id):
    circle = Circle.objects.get(id=id)
    return render(request, 'circle.html', {'circle':circle})

def new(request, id):
    new = Circle.objects.get(id=id)
    
    return render(request, 'new.html', {'new':new})

def about(request):
    info = Info.objects.order_by('-date')[:1]
    return render(request, 'about.html', {'infos':info})

def director(request):
    director = Director.objects.order_by('-date')[:1]
    return render(request, 'director.html', {'directors':director})