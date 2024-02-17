from django.shortcuts import render
from app1.models import Student,Category
from app1.forms import studentform

def view(request):
    b=Student.objects.all()
    return render(request,'view.html',{'b':b})
def add(request):
    form=studentform()
    if(request.method=="POST"):
        form=studentform(request.POST)
        if(form.is_valid()):
            form.save()
            return view(request)
    return render(request,'add.html',{'form':form})

def add1(request,p):
    b=Student.objects.get(id=p)
    form=studentform(instance=b)
    if(request.method=="POST"):
        form=studentform(request.POST,instance=b)
        if(form.is_valid()):
            form.save()
            return view(request)
    return render(request,'add.html',{'form':form})

def view1(request,p):
    k=Student.objects.get(id=p)
    return render(request,'view1.html',{'k':k})

def detail_delete(request,p):
    f=Student.objects.get(id=p)
    f.delete()
    return view(request)

