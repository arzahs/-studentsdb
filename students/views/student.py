# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from students.models import Student 
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
def student_list(request):
	students = Student.objects.all();
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()
	paginator = Paginator(students, 3)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		students = paginator.page(1)
	except EmptyPage:
		students = paginator.page(paginator.num_pages)
	groups = ({'name':'mf111'}, {'name':'mf112'}, {'name':'mf113'})
	return render(request, 'students/students_list.html', {"students": students, "groups": groups})

def students_add(request):
	return HttpResponse('here will be form students')

def students_edit(request, sid):
	return HttpResponse('here will be form students %s' % sid)

def students_visiting(request, sid):
	return HttpResponse('visiting %s' % sid)

def students_delete(request, sid):
	return HttpResponse('delete %s' % sid)


def journal(request):
	return render(request, 'students/records.html', {})
