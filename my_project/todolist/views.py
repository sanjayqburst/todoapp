from .models import Todolist
from django.shortcuts import render

# Create your views here.


def index(request):
    todo_items = Todolist.objects.order_by('id')
    context = {"todo_items": todo_items}
    return render(request, 'todolist/index.html', context)
