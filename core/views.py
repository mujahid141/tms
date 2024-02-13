from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializers , UserSerializers
from .models import Task , User , Category



def hello(request):
       return render(request,'home.html')

@api_view(['GET'])
def Tasks(request):
       tasks = Task.objects.all()
       serializer = TaskSerializers(tasks, many= True)
       return Response(serializer.data)

@api_view(['GET'])
def Users(request):
       user = User.objects.all()
       serializer = UserSerializers(user, many= True)
       return Response(serializer.data)
       


# Create your views here.
