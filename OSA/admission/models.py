from django.db import models


# Create your models here.

class Patient(models.Model):
	pt_first_name = models.CharField(max_length=30)
	pt_last_name = models.CharField(max_length=30)
	time_added = models.DateTimeField('time added')
	pt_number = models.CharField(max_length=7)
	pt_dob = models.DateField('date of birth')
	presenting_condition = models.CharField(max_length=200)
	# Defining the acute medicine consultants and the senior review field
	RUSSELL = 'ER'
	STOSIC = 'JS'
	BLACKBURN = 'AB'
	VENU = 'MV'
	NONE = 'None'
	SENIOR_REVIEW_CHOICES = (
		(RUSSELL, 'Dr Russell'),
		(STOSIC, 'Dr Stosic'),
		(BLACKBURN, 'Dr Blackburn'),
		(VENU, 'Dr Venu'),
		(NONE, 'None yet')
	)
	senior_review = models.CharField(max_length=4, choices=SENIOR_REVIEW_CHOICES, default=NONE)
	# Defining the original referer of the patient in a similar way
	EMERGENCYDEPARTMENT = 'ED'
	GENERALPRACTICE = 'GP'
	ORIGINAL_REFERER_CHOICES = (
		(EMERGENCYDEPARTMENT, 'Emergency Department'),
		(GENERALPRACTICE, 'By their GP'),
	)
	origin = models.CharField(max_length=2, choices=ORIGINAL_REFERER_CHOICES, default=GENERALPRACTICE)
	clerked_by = models.CharField(max_length=100)
	location = models.CharField(max_length=20)
	jobs = models.CharField(max_length=100)
	def __str__(self):
		return '%s %s %s %s' % (self.pt_first_name, self.pt_last_name, self.pt_dob, self.pt_number)

