from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .get_translation.load_tran import Translation

data_path=""
model_path=""
model=Translation(data_path,model_path)


def get_res(request):
    req_get=request.GET
    src=req_get['src']
    lab=req_get['lab']
    tgt=model.get_trans(src+lab)
    return JsonResponse({'tgt':tgt})

def index(request):
    return render(request,'index.html')