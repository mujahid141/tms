from django.db import models

class User(models.Model):
    userName = models.CharField(primary_key=True,max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Category(models.Model):
    title = models.CharField(max_length=40, primary_key=True)
    discription =  models.CharField(max_length=255, null= True)
    

class Task(models.Model):
    taskName = models.CharField(max_length= 255)
    discription = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    startingDate = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    
