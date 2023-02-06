from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from .forms import Todoforms
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=='POST':
        firstname = request.POST['first_name']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password1)
                user.save()
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('task_view')
        else:
            messages.info(request, "invalid details")
            redirect('login')
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')

def task_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority,date=date)
        obj.save()
    obj1 = Task.objects.all()
    return render(request,'task_view.html',{'objs':obj1})

def delete(request, id):
    obj=Task.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('task_view')
    return render(request, 'delete.html', {'obj':obj})
def update(request,id):
    obj=Task.objects.get(id=id)
    form=Todoforms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('task_view')
    return render(request, 'update.html',{'obj':obj, 'form':form})

def detail(request, id):
    obj = Task.objects.get(id=id)
    return render(request, 'detail.html', {'i':obj})



# class TaskListView(ListView):
#     model = Task
#     template_name = 'task_view.html'
#     context_object_name = 'objs'
# class TaskDetailView(DetailView):
#     model = Task
#     template_name = 'detail.html'
#     context_object_name = 'i'
# class TaskUpdateView(UpdateView):
#     model = Task
#     template_name = 'edit.html'
#     context_object_name = 'task'
#     fields = ['name', 'priority', 'date']
#     def get_success_url(self):
#         return reverse_lazy('detail',kwargs={'pk':self.object.id})
# class TaskDeleteView(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('task_view')

