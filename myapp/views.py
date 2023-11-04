from django.shortcuts import render
from django.http import HttpResponse
from . models import place


# Create your views here.
# def demo(request):
#     return(render(request,"home.html"))
# def addition(request):
#     x=request.GET['n1']
#     y=request.GET['n2']
#     res=x+y
#     return(render(request,"result.html",{'obj':res}))
def home(request):
    obj=place.objects.all()


    return render(request,'index.html',{'result':obj})