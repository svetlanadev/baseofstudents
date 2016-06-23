from __future__ import unicode_literals
from django.db import models


class Studentsprofile(models.Model):
	firstname = models.CharField(max_length= 50)
	lastname = models.CharField(max_length= 50)
	middlename = models.CharField(max_length= 50)
	dait_of_birth = models.DateField()
	# photo = models.ImageField(upload_to='ProfileImage', blank=True)
	students_ticket = models.IntegerField(default=0)
	# group_of_student = ForeignKey(Groupofstudents)


	def __unicode__(self):
		return self.firstname


