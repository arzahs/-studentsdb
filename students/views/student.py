# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from students.models import Student, Group 
from django.core.urlresolvers import reverse
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.generic import UpdateView
from django.forms import ModelForm
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
	groups = Group.objects.all()
	return render(request, 'students/students_list.html', {"students": students, "groups": groups})

def students_add(request):
	if request.method == 'POST':
		if request.POST.get('add_button') is not None:
			data = {
			'middle_name' : request.POST['middle_name'],
			'notes' : request.POST['notes'],
			}
			errors = {}
			#validation input
			first_name = request.POST['first_name'].strip()
			if not first_name:
				errors['first_name'] = u"Name is required"
			else:
				data['first_name'] = first_name
			
			last_name = request.POST['last_name'].strip()
			if not last_name:
				errors['last_name'] = u"Last name is required"
			else:
				data['last_name'] = last_name
			
			birthday = request.POST.get('birthday','').strip()
			if not birthday:
				errors['birthday'] = u"Birthday is required"
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except ValueError:
					errors['birthday'] = u'Input correct date YYYY-MM-DD'
				else:
					data['birthday'] = birthday
			
			ticket = request.POST['ticket'].strip()
			if not ticket:
				errors['ticket'] = u"Ticket is required"
			else:
				data['ticket'] = ticket
			
			photo = request.FILES.get('photo','')
			if photo:
				data['photo'] = photo
			
			students_group = request.POST.get('student_group','').strip()
			if not students_group:
				errors['group'] = u'Input group'
			else:
				groups = Group.objects.filter(pk=students_group)
				if len(groups) != 1:
					errors['group'] = u'Input correctly group'
				else:
					data['student_group'] = groups[0]
			
			#если нет ошибок ввода
			if not errors:
				student =Student(**data)
				student.save()
				return HttpResponseRedirect(u'%s?status_message=Student has been added!' % reverse('home'))
			else:
				return render(request, 'students/student_add.html', {'groups': Group.objects.all().order_by('title'), 'error': errors})
		
		elif request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect(u'%s?status_message=Adding a student has been canceled!' % reverse('home'))
	else:
		return render(request, 'students/student_add.html', {'groups': Group.objects.all().order_by('title')})

# class StudentForm(ModelForm):
    
#     class Meta:
#         model = Student
#         fields = '__all__'

        
class StudentUpdateView(UpdateView):
	model = Student
	fields = '__all__'
	template_name = 'students/student_edit.html'
	#form_class = StudentForm
	
	def get_success_url(self):
		#return '/'
		#return u'%s/?status_message=Student has been saved!'% reverse('home')
		return u'%s?status_message=Student has been saved!' % reverse('home')
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Changing a student has been canceled!' %reverse('home'))
		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)

def students_visiting(request, sid):
	return HttpResponse('visiting %s' % sid)

def students_delete(request, sid):
	return HttpResponse('delete %s' % sid)


def journal(request):
	return render(request, 'students/records.html', {})
