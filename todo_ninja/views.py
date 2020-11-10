from django.shortcuts import render

def index(request, **kwargs):
    template_name = "todo_ninja/task_index.html"
    return render(request, template_name)