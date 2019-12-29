# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models  import ToDo
def home(request):
    tasks = ToDo.objects.all()
    context ={'tasks':tasks}
    return render(request,'tasks/index.html',context)

def add_subject(request):
      print (request.POST)
      content =request.POST['name']

      todo =ToDo(content=content)
      todo.save()
      return redirect('/')


def edit(request,sr_no):
    tasks =ToDo.objects.get(pk=sr_no)
    context ={'tasks':tasks}
    return render(request,'tasks/edit.html',context)

def update(request,sr_no):
    print(request.POST )
    tasks =ToDo.objects.get(pk=sr_no)
    print(tasks)
    tasks.content = request.POST['name']
    tasks.save()
    return redirect('/')

def delete(request,sr_no):
   data =ToDo.objects.get(pk=sr_no)
   data.delete()
   return redirect('/')
