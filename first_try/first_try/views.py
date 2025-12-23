from django.shortcuts import render

# Create your views here.
def nate(request):
    return render(request,"index.html")

def car(request):
    return render(request,"car.html")