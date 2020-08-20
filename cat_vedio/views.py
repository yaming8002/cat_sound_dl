from django.shortcuts import render
from django.http import HttpResponse
from .cat_vedio_DL import cat_vedio_DL
# numba指定版本0.48
# pip install numba==0.48
# pytube指定版本3 不用等號
# pip install pytube3
import sys
from django.http import HttpResponseRedirect
import json

# Create your views here.

def cat_view(request):
    return render(request, 'cat_sound.html')

def data_back(request):
    print(request)
    if request.GET:
        test_path=request.GET['vedio_id']
        print("===========================",test_path)
        # test_path=sys.argv
        a = cat_vedio_DL()
        a.downMp4toW(test_path)
        # predict_answer=str(a.test_ans_show( test_path))
        predict_answer=a.test_ans_show_tostr(test_path)
        # predict_answer=a.test_ans_show( test_path)
        # print(predict_answer)
        return HttpResponse(predict_answer)
