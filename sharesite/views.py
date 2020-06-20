from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
import requests
# Create your views here.
def sharePage(request):
    if request.method == "GET":
        print(' An filled Form*****************************************')
        form = PostForm(request.GET)
        data = request.GET.copy()
        print(data.get('hashTags'))
        if( form.is_valid()):
            form.save()
            return render(request,'sharePage.html',{'text':request.GET['Text'],'hashtag':request.GET['hashTags'],'url':request.GET['URL'],'form':form})
    else:
        print(' An Empty Form*****************************************')
        form = PostForm()
    try:
        return render(request,'sharePage.html',{'text':request.GET['Text'],'hashtag':request.GET['hashTags'],'url':request.GET['URL'],'form':form})
    except:
        return render(request,'sharePage.html',{'form':form})
def homePage(request):
    return render(request,'index.html',{})

def Instructions(request):
    return render(request, 'about.html',{})
