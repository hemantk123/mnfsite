from django.db import models

# Create your models here.
class personal_info_add(models.Model):
	#CHOICES = [
	#	('webd','Web Developer'),
	#	('datasci','Data Scientist'),
	#]
	name=models.CharField(max_length=40)
	profession=models.CharField(max_length=50)
	#profession=models.CharField(
	#	                        max_length=20,
	#	                        choices=CHOICES,		                      
	#	                        )
	address=models.TextField()

	def __str__(self):
		return self.name