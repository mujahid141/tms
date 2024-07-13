from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=40, primary_key=True)
    discription =  models.CharField(max_length=255, null= True)
    

class Task(models.Model):
    taskName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    startingDate = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.taskName