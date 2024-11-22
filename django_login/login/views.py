from django.shortcuts import render

def index(request):
    return render(request, 'authentication/login.html')
def base(request):
    return render(request, 'base.html')