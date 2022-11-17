from django.db import models


# Create your models here.
class studentdata(models.Model):
	name = models.CharField(max_length=50)
	rollnumber = models.IntegerField()
	department = models.TextField()
	stud_class = models.TextField()
	phonenumber = models.IntegerField()
	email = models.EmailField(unique=True)
	def __str__(self):
		return self.name

