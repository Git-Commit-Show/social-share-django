from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
import requests
# Create your views here.
def sharePage(request):
    if request.method == "GET":
        form = PostForm(request.GET)
        data = request.GET.copy()
        print(data.get('hashTags'))
        if( form.is_valid()):
            form.save()
            return render(request,'sharePage.html',{'text':request.GET['Text'],'hashtag':request.GET['hashTags'],'url':request.GET['URL'],'form':form})
    else:
        form = PostForm()

    return render(request,'sharePage.html',{'text':request.GET['Text'],'hashtag':request.GET['hashTags'],'url':request.GET['URL'],'form':form})
