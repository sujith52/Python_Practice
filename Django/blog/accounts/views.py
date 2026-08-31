from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    main = '''<h2>hello there thi is the html code for the djo see </h2> <ol><li>Hello world</li></ol>'''
    return HttpResponse(main, content_type ="text/html")

def mains(req):
    print(req)
    return HttpResponse("hi there ")