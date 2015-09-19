# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from students.models import Group
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView, CreateView
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse
def groups_list(request):
	groups = Group.objects.all()
	paginator = Paginator(groups, 5)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		groups = paginator.page(1)
	except EmptyPage:
		groups = paginator.page(paginator.num_pages)
	return render(request, 'students/groups_list.html', {"groups": groups})

class GroupForm(ModelForm):
    
	class Meta:
		model = Group
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(GroupForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		
		if kwargs['instance'] is None:
			add_form = True
		else:
			add_form = False
		# set form tag attributes
		if add_form:
			self.helper.form_action = reverse('group_add')
		else:
			self.helper.form_action = reverse('group_edit', kwargs={'pk': kwargs['instance'].id})
		
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
		# add buttons
		# self.helper.layout[-1] = FormActions(
		# Submit('add_button', u'Save', css_class="btn btn-primary"),
		# Submit('cancel_button', u'Cancel', css_class="btn btn-link"),)
		self.helper.add_input(Submit('add_button', u'Save')) 
		self.helper.add_input(Submit('cancel_button', u'Cancel')) 

class BaseGroupView(object):
	def get_success_url(self):
		return u'%s?status_message=Group has been saved!'% reverse('groups_list')

	def post(self, request, *args, **kwargs):
        # handle cancel button
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(reverse('groups_list') +u'?status_message=Editing canceled.')
		else:
			return super(BaseGroupView, self).post(request, *args, **kwargs)

class GroupCreateView(BaseGroupView,CreateView):
	model = Group
	template_name = 'groups/groups_add.html'
	form_class = GroupForm
	

class GroupUpdateView(BaseGroupView,UpdateView):
	model = Group
	template_name = 'groups/groups_add.html'
	form_class = GroupForm

class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'groups/group_confirm_delete.html'

	def get_success_url(self):
		#return '/'
		#return u'%s/?status_message=Student has been saved!'% reverse('home')
		return u'%s?status_message=Group has been deleted!' % reverse('groups_list')

	# def post(self, request, *args, **kwargs):
	# 	try:
	# 		return HttpResponseRedirect(reverse('groups_list') +u'?status_message=Group deleting.')
	# 	except:
	# 		return HttpResponseRedirect(reverse('groups_list') +u'?status_message=Group deleting error.')