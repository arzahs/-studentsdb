from django.views.generic.base import TemplateView
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.core.urlresolvers import reverse
from students.models import MonthJournal, Student
from ..util import paginate

class JournalView(TemplateView):
	template_name = 'students/journal.html'

	def get_context_data(self, **kwargs):
		context = super(Journal, self).get_context_data(**kwargs)

		today = datetime.today()
		month = date(today.year, today.month, 1)

		context['prev_month'] = '2015-10-01'
		context['next_month'] = '2015-08-01'
		context['year'] = 2015
		context['cur_month'] = '2015-09-01'
		context['month_verbose'] = u'September'
		context['month_header'] = [
			{'day':1, 'verbode':'Пн'},
			{'day':2, 'verbode':'Вт'},
			{'day':3, 'verbode':'Ср'},
			{'day':4, 'verbode':'Чт'},
			{'day':5, 'verbode':'Пт'},
		]

		queryset = Student.objects.order_by('last_name')

		update_url = reverse('journal')

		students = []

		for student in queryset:
			days = []
			for day in range(1, 31):
				days.append({
					'day':day,
					'present': True,
					'date': date(2015, 7, day).strftime('%Y-%m-%d'),
					})
			students.append({
				'fullname': u'%s %s' % (student.last_name, student.first_name),
				'days': days,
				'id':student.id,
				'update_url': update_url,
				})

		context = paginate(students, 10, self.request, context, var_name='students')
		return context