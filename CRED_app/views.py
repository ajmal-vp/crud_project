from django.shortcuts import render, redirect

from CRED_app.forms import TodoForm
from CRED_app.models import Todo


# Create your views here.
def home(request):
     return render(request,'home.html')


# create
def index(request):

     form = TodoForm()

     if request.method == "POST":

          form1 = TodoForm(request.POST)
          if form1.is_valid():
               form1.save()



     return render(request,'index.html',{"form":form})


# read

def read(request):
     data = Todo.objects.all()

     return render(request,"read.html",{"data":data})

def delete_data(request,id):
    data = Todo.objects.get(id=id)
    print(data)
    data.delete()
    return redirect('read')


    return render(request,'read.html')

def update_data(request,id):
    data = Todo.objects.get(id=id)
    print("data",data)
    form = TodoForm(instance=data)
    print(form)

    if request.method == 'POST':
        data = TodoForm(request.POST,instance= data)
        if data.is_valid():
            data.save()
            return redirect("read")




    return render(request,"update.html",{"form":form})
