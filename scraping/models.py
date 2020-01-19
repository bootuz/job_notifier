from django.db import models

# Create your models here.


class Job(models.Model):
    link = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

