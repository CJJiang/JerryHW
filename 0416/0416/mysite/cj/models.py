from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=10)
	gender = models.CharField(max_length=5)
	address = models.CharField(max_length=50, blank=True)
	interest = models.CharField(max_length=50)
	autobiography = models.CharField(max_length=100)

	def __str__(self):
		return self.name