from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from cmdb.models import Show
from cmdb import models
import csv,os
import json
def index(request):
    return render(request,'index.html')
def search(request):
    if request.method == 'POST':
        res = request.POST.get('Search')
        if res=='Search':
            q = request.POST.get('searchthings')
            blogs = Show.objects.filter(name=q)
            if blogs:
                obj = Show.objects.get(name=q)
                hit = obj.hit
                hit += 1
                Show.objects.filter(name=q).update(hit=hit)
                return render(request, 'result.html', {'blogs': blogs})
            return render(request, 'error.html')
def MySQL(request):
    if request.method == "POST":
        myFile =request.FILES.get("myfile",None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return render(request,'uploaderror.html')
        destination = open(os.path.join("C:\\Users\win7\PycharmProjects\FY_DE_Gaoxiaoyu",myFile.name),'wb+')
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        res1 = request.POST.get('upload')
        if res1 == 'upload':
            with open(myFile.name,'r') as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    Show.objects.create(name=row[0], description=row[1],example=row[2],hit=row[3])
            return render(request, 'success.html')
        return render(request, 'uploadsuccess.html')
def Echarts(request):
    name_list = []
    hit_list = []
    for a in models.Show.objects.order_by('-hit')[:5]:
        name_list.append(a.name)
        hit_list.append(a.hit)
    data=list(zip(name_list,hit_list))
    return render(request, 'echarts.html',{ 'List':json.dumps(data)})


