from django.shortcuts import render
import requests
from PIL import Image
from .forms import ImageForm
from media.images import main
import os

INPUT = "oppojuhiji0[9h08h.jpg"
OUTPUT='watermarkAdded.jpg'
logo='download.jpg'
position='tl'
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
			imdt=logoPath.split('/')
			logo=imdt[1]
			try:
				os.chdir('C:/Users/pc/Desktop/Social- share/socialShare/media/images')
				main.watermark(logo,request.POST['position'],request.POST['text'])
				print('It worked')
			except Exception as e:
				print(e)
				print("Not working")
	context= {'form': form}
	return render(request,'upload.html',context)


