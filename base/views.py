from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_detail.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')