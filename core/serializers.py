from rest_framework.serializers import ModelSerializer
from .models import Task , User

class TaskSerializers(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'