from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    return HttpResponse("<h1> hii...hello</h1>")


def view2(request,email):
    return render(request,"view2.html",context={'email':email,'name':"Kavya"})

def view3(request,name):
    return HttpResponse(f'<h1>hello Mr/miss {name}</h1>')

def if_demo(request):
    login=True
    return render(request,"if_demo.html", context={'login':login})

def ifelse_demo(request):
    login=False
    return render(request,"ifelse_demo.html", context={'login':login})

def for_demo(request):
    return render(request,"for_demo.html",context={"items":['apple','ball','cat'],\
        'profile':{'name':"kavya",'age':23,'sal':1000}})

# Create your views here.
