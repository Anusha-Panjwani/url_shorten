from django.db import models

# Create your models here.

class bitly(models.Model):
	long_url = models.URLField()
	model_short_code = models.CharField(max_length=6)
	count = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.model_short_code