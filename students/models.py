from __future__ import unicode_literals
from django.db import models
from parametry.models import Groupofstudents


class Studentsprofile(models.Model):
	firstname = models.CharField(max_length= 50)
	lastname = models.CharField(max_length= 50)
	middlename = models.CharField(max_length= 50)
	date_of_birth = models.DateField()
	# photo = models.ImageField(upload_to='ProfileImage', blank=True)
	students_ticket = models.IntegerField(default=0)
	group = models.ForeignKey(Groupofstudents)


	def __unicode__(self):
		return self.firstname


