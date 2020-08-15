from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse   #this isonly for printing simple sentence

#for html file we willuse render

def home(request):
    return render(request,'index.html',{'name':'kapil pandey'})
    
def add(request):
    var1=int(request.POST['num1'])
    var2=int(request.POST['num2'])
    res=var1+var2
    
    return render(request,'result.html',{'result':res,'var1':var1,'var2':var2})