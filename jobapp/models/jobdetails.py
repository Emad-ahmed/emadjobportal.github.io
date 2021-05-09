from django.db import models
from 

class JobInfo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skill = models.TextField()
    time_of_work = models.IntegerField()
    last_date_of_application = models.DateTimeField()
    city = models.CharField(max_length=100)
    salary_tk = models.IntegerField()
    images = models.ImageField(upload_to='images/')
