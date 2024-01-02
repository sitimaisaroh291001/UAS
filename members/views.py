from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.template import loader

from .models import Member

def members(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

# Create your views here.

def members(request):
    mem=Member.objects.all()
    return render(request,'home.html',{'mem':mem})

def add(request):
    return render (request,'add.html')

def profil(request):
  return render(request, 'profil.html')
  
def addrec(request):
    x=request.POST['input1']
    y=request.POST['input2']
    z=request.POST['input3']
    mem=Member(input1=x,input2=y,input3=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})


def uprec(request,id):
    x=request.POST['input1']
    y=request.POST['input2']
    z=request.POST['input3']
    mem=Member.objects.get(id=id)
    mem.input1=x
    mem.input2=y
    mem.input3=z
    mem.save()
    return redirect("/")

