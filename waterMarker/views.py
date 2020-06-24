from django.shortcuts import render
import requests
from PIL import Image
from .forms import ImageForm
from media.images import image
import os

INPUT = "Common_Event_Poster_Verticle_Withlogo.png"
OUTPUT = "static/result.png"
POSITION='bcl'
DISPLAY = False
TEXT = ""                               # Let it be empty unless you want text and watermark both
FONT = "fonts/Helvetica.ttf"
COLOR = "white"
TEXT_SIZE = 40
TEXT_POSITION = "bc"
TEXT_ALIGN_WATERMARK = "r"
# Create your views here.
def upload(request):
	logoPath=''
	form= ImageForm(request.POST or None, request.FILES or None)
	if(request.method=='POST'):
		if form.is_valid():
			form.save()
			initial_obj = form.save(commit=False)
			initial_obj.save()
			logoPath=initial_obj.logo.name
			imdt=logoPath.split('/',1)
			logo=imdt[1]
			print(logo)
			print(os.getcwd())
			try:
			    print(os.getcwd())
			    os.chdir('media/images')
			    if(request.POST['path']):
			    	image.watermark_a_folder(request.POST['path'])
			    image.watermark(INPUT,OUTPUT,logo,request.POST['position'],request.POST['text'])
			    print('It worked')
			except Exception as e:
				print(e)
				print("Not working")
	context= {'form': form}
	return render(request,'upload.html',context)


def viewAll(request):
	print(os.getcwd())
	list=os.listdir('static/')
	return render(request,'view.html',{'list':list})

