from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def get_res(request):
    req_get=request.GET
    src=req_get['src']
    lab=req_get['lab']
    return JsonResponse({'tgt':src+lab})

def index(request):
    return render(request,'index.html')