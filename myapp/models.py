
from django.db import models

class Books(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	authors = models.CharField(max_length=200)
	pub_date = models.CharField(max_length=20)
	publisher = models.CharField(max_length=200)
	summary = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	link = models.CharField(max_length=2083)
	cover = models.CharField(max_length=2083)
