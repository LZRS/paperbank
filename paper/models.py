from __future__ import unicode_literals

from django.db import models

from .model_tools import uploaded_paper_name 
# Create your models here.

class Subject(models.Model):
   """
   Model to keep track of the subjects
   available for the papers
   """
   name = models.CharField(max_length=40)
   
   def __str__(self):
       return self.name



class Paper(models.Model):
    """
    This is the main model to 
    hold the uploaded papers
    """
    name = models.CharField(max_length=50)
    paper_file = models.FileField(upload_to=uploaded_paper_name)
     
    subjects = models.ForeignKey(Subject)

    def __str__(self):
        return self.name

