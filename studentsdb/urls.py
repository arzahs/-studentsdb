"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, DEBUG
from students.views.student import StudentUpdateView, StudentDeleteView
from students.views.group import GroupCreateView, GroupUpdateView, GroupDeleteView
from students.views.journal import JournalView
urlpatterns = [
    #Students urls
    url(r'^students/add/$', 'students.views.student.students_add', name='students_add'),
    url(r'^students/(?P<pk>[0-9]+)/edit/$',  StudentUpdateView.as_view(), name='students_edit'),
	url(r'^students/(?P<sid>[0-9]+)/visiting/$', 'students.views.student.students_visiting', name='students_visiting'),  
    url(r'^students/(?P<pk>[0-9]+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),
    #Groups
    url(r'^groups/$', 'students.views.group.groups_list', name='groups_list'),
    url(r'^groups/add/$', GroupCreateView.as_view(), name='group_add'),
    url(r'^groups/(?P<pk>[0-9]+)/edit/$', GroupUpdateView.as_view(), name='group_edit'),
    url(r'^groups/(?P<pk>[0-9]+)/delete/$', GroupDeleteView.as_view(), name='group_delete'),
    #Journal
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
    url(r'^admin/', include(admin.site.urls)),
    #debug media 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT,}),
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),

    #------
    url(r'^', 'students.views.student.student_list', name='home'),

] 

