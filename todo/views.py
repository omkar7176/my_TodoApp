from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.
def todo_list(request):
    return render(request, 'todo/index.html')

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
    
    return redirect('todo_list')