from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb.models import Show
# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("Hello World")
   # return render(request,"index.html",)
    #if request.method=="POST":
    #    searchthings=request.POST.get("searchthings",None)
     #   print(searchthings)
    #return render(request,"index.html",)
def search(request):
    q=request.POST.get('searchthings')
    blogs=Show.objects.filter(name=q)
    if blogs:
        return render(request,'result.html',{'blogs':blogs})
    return render(request, 'error.html')

