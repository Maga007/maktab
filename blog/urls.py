from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),# + +
    path('teachers/', views.teachers, name='teachers'),# + +
    path('circles/', views.circles, name='circles'),# + +
    path('sertificat/', views.setificat, name='sertificat'),# + +
    path('meetings/', views.meetings, name='meetings'),# + +
    path('events/', views.events, name="events"),# + +
    path('news/', views.news, name='news'),# + +
    path('meeting/<int:id>/', views.meeting, name="meeting"),# + +
    path('event/<int:id>', views.event, name="event"),# + +
    path('teacher/<int:id>/', views.teacher, name='teacher'),# ++
    path('circle/<int:id>/', views.circle, name='circle'),# +
    path('new/<int:id>/', views.new, name='new'),# + +
    path('director/', views.director, name='director'),#
    path('about', views.about, name='about')# +
]