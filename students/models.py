# -*- coding: utf-8 -*-

from django.db import models
from parametry.models import Groupofstudents


class Studentsprofile(models.Model):
	firstname = models.CharField(max_length= 50, verbose_name=u'Імя')
	lastname = models.CharField(max_length= 50, verbose_name=u'Призвіще')
	middlename = models.CharField(max_length= 50, verbose_name=u'По батькові')
	date_of_birth = models.DateField(verbose_name=u'Дата народження')
	photo = models.ImageField(upload_to='profile_photo', blank=True)
	students_ticket = models.IntegerField(default=0, verbose_name=u'№ Білету')
	group = models.ForeignKey(Groupofstudents, null=True, blank=True, verbose_name=u'Група')


	def __str__(self):
		return self.firstname
 
