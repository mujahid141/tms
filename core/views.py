from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import get_object_or_404, redirect
from .models import Task , User , Category



def hello(request):
       return render(request,'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tasks')  # Redirect to a success page.
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_tasks(request):
    # Get tasks for the current user
    tasks = Task.objects.filter(user=request.user)
    
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context)


def toggle_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('tasks')