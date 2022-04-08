from django.shortcuts import render
from django.http import HttpResponse

def render_a_template(request):
    return render(request, 'renderme.html', {"msg":"Hello World!"})