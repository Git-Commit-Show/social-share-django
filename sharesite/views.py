from django.shortcuts import render
from .forms import PostForm
import requests
# Create your views here.
def sharePage(request):
    return render(request, 'sharePage.html')
    '''
	if request.method == "GET":
		form = PostForm(request.GET)
		data = request.GET.copy()
		print(data.get('hashTags'))
		if( form.is_valid()):
			form.save()
	else:
		form = PostForm()
	return render(request,'sharePage.html',{'text':request.GET['Text'],'hashtag':request.GET['hashTags'],'url':request.GET['URL'],'form':form})
    '''
