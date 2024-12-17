from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def dyballa(request):
    template=loader.get_template("dyballa.html")
    return HttpResponse(template.render())

def submit(request):
    template=loader.get_template('submit.html')
    return HttpResponse(template.render())
 