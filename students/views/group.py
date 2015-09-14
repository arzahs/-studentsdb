# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from students.models import Group
def groups_list(request):
	groups = Group.objects.all()
	return render(request, 'students/groups_list.html', {"groups": groups})
def groups_edit(request, sid):
	return HttpResponse('group edit %s'% sid)

def groups_delete(request, sid):
	return HttpResponse('group delete %s'% sid)