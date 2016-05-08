# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from students.models import Student, Group
from django.core.urlresolvers import reverse
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from ..util import paginate, get_current_group

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.utils.translation import ugettext as _


def student_list(request):
    current_group = get_current_group(request)

    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
        students = Student.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    context = paginate(students, 9, request, {}, var_name='students')
    return render(request, 'students/students_list.html', context)


@login_required
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
                errors['first_name'] = _(u"Name is required")
            else:
                data['first_name'] = first_name

            last_name = request.POST['last_name'].strip()
            if not last_name:
                errors['last_name'] = _(u"Last name is required")
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday','').strip()
            if not birthday:
                errors['birthday'] = _(u"Birthday is required")
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except ValueError:
                    errors['birthday'] = _(u'Input correct date YYYY-MM-DD')
                else:
                    data['birthday'] = birthday

            ticket = request.POST['ticket'].strip()
            if not ticket:
                errors['ticket'] = _(u"Ticket is required")
            else:
                data['ticket'] = ticket

            photo = request.FILES.get('photo','')
            if photo:
                data['photo'] = photo

            students_group = request.POST.get('student_group','').strip()
            if not students_group:
                errors['group'] = _(u'Input group')
            else:
                groups = Group.objects.filter(pk=students_group)
                if len(groups) != 1:
                    errors['group'] = _(u'Input correctly group')
                else:
                    data['student_group'] = groups[0]

            #если нет ошибок ввода
            if not errors:
                student =Student(**data)
                student.save()
                return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'),
                                                                       _(u'Student has been added')))
            else:
                return render(request, 'students/student_add.html', {'groups': Group.objects.all().order_by('title'), 'error': errors})

        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'),
                                                                   _(u'Student adding has been canceled')))
    else:
        return render(request, 'students/student_add.html', {'groups': Group.objects.all().order_by('title')})


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # set form tag attributes
        self.helper.form_action = reverse('students_edit',kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', _(u'Save'), css_class="btn btn-primary"),
            Submit('cancel_button', _(u'Cancel'), css_class="btn btn-link"),)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDeleteView, self).dispatch(
            *args, **kwargs)

    def get_success_url(self):
        #return '/'
        #return u'%s/?status_message=Student has been saved!'% reverse('home')
        return u'%s?status_message=Student has been deleted!' % reverse('home')


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/student_edit.html'
    form_class = StudentForm

    def get_success_url(self):
        #return '/'
        #return u'%s/?status_message=Student has been saved!'% reverse('home')
        return u'%s?status_message=%s' % (reverse('home'), _(u"Student has been saved!"))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentUpdateView, self).dispatch(
            *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'),
                                                                   _(u'Changing a student has been canceled!')))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

def students_visiting(request, sid):
    return HttpResponse('visiting %s' % sid)

def students_delete(request, sid):
    return HttpResponse('delete %s' % sid)


def journal(request):
    return render(request, 'students/records.html', {})
