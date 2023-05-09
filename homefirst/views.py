from django.shortcuts import render,HttpResponse
from homefirst.models import contact
from datetime import datetime
# Create your views here.
def index(request):
    context={
        'var':"this is variable"
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def version(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def sub(request):
    if request.method=="POST":
        name=request.POST.get('name')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        cont=contact()
        cont.name=name
        cont.pno=pno
        cont.email=email
        cont.desc=desc
        cont.save()
    return render(request,'contact.html')