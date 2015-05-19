from django.db import models
from datetime import datetime

# Create your models here.
class SkillsStudents(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    skills = models.CharField(max_length=150)
    cdate = models.DateTimeField('date created', default = datetime.now)