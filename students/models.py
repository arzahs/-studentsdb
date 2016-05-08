from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Student(models.Model):
	"""Student Model"""
	class Meta(object):
		verbose_name=_(u'Student')
		verbose_name_plural=_(u'Students')

	first_name =models.CharField(max_length=256, blank=False, verbose_name=_(u'Name'))
	last_name = models.CharField(max_length=256, blank=False, verbose_name=_(u'Last Name'))
	middle_name = models.CharField(max_length=256, blank=True, verbose_name=_(u'Middle Name'), default='')
	birthday = models.DateField(blank=False, verbose_name=_(u'Birthday'))
	photo = models.ImageField(blank=True, verbose_name=_(u'Photo'))
	ticket = models.CharField(max_length=256, blank=False, verbose_name='Ticket')
	student_group = models.ForeignKey('Group',
		verbose_name=_(u'Group'), 
		blank=True, null=True, on_delete=models.PROTECT)
	notes = models.TextField(blank=True, verbose_name=_(u'Notes'), default='')

	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Group(models.Model):
	"""docstring for Group"""
	class Meta(object):
		verbose_name=_(u'Group')
		verbose_name_plural=_(u'Groups')

	title =models.CharField(max_length=256, blank=False, verbose_name=_(u'Title'))
	notes = models.TextField(blank=True, verbose_name=_(u'Notes'), default='')	
	leader = models.OneToOneField('Student',
	verbose_name=_(u'Leader'),
	blank=True,
	null=True,
	on_delete = models.SET_NULL)
	def __str__(self):
		return u'%s' % (self.title)

class MonthJournal(models.Model):
	class Meta(object):
		verbose_name=_(u'MonthJournal')
		verbose_name_plural=_(u'MonthJournals')

	student = models.ForeignKey('Student', verbose_name=_(u'Student'),blank = False, unique_for_month='date')
	date = models.DateField(verbose_name=_(u'Date'), blank=False)
	
	present_day1 = models.BooleanField(default=False)
	present_day2 = models.BooleanField(default=False)
	present_day3 = models.BooleanField(default=False)
	present_day4 = models.BooleanField(default=False)
	present_day5 = models.BooleanField(default=False)
	present_day6 = models.BooleanField(default=False)
	present_day7 = models.BooleanField(default=False)
	present_day8 = models.BooleanField(default=False)
	present_day9 = models.BooleanField(default=False)
	present_day10 = models.BooleanField(default=False)
	present_day11 = models.BooleanField(default=False)
	present_day12 = models.BooleanField(default=False)
	present_day13 = models.BooleanField(default=False)
	present_day14 = models.BooleanField(default=False)
	present_day15 = models.BooleanField(default=False)
	present_day16 = models.BooleanField(default=False)
	present_day17 = models.BooleanField(default=False)
	present_day18 = models.BooleanField(default=False)
	present_day19 = models.BooleanField(default=False)
	present_day20 = models.BooleanField(default=False)
	present_day21 = models.BooleanField(default=False)
	present_day22 = models.BooleanField(default=False)
	present_day23 = models.BooleanField(default=False)
	present_day24 = models.BooleanField(default=False)
	present_day25 = models.BooleanField(default=False)
	present_day26 = models.BooleanField(default=False)
	present_day27 = models.BooleanField(default=False)
	present_day28 = models.BooleanField(default=False)
	present_day29 = models.BooleanField(default=False)
	present_day30 = models.BooleanField(default=False)
	present_day31 = models.BooleanField(default=False)

	def __str__(self):
		return u'%s: %d, %d' % (self.student.last_name, self.date.month,
            self.date.year)

