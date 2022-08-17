
from django.shortcuts import render
from .models import Place
from.models import Peam

def demo(request):
    obj = Place.objects.all()
    peoples = Peam.objects.all()



    return render(request,"index.html",{'result':obj,'peeps':peoples})
