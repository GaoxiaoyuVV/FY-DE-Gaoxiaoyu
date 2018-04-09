from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
   # return HttpResponse("Hello World")
   # return render(request,"index.html",)
    if request.method=="POST":
        searchthings=request.POST.get("searchthings",None)
        print(searchthings)
    return render(request,"index.html",)
