from django.shortcuts import render
import requests
from PIL import Image
from .forms import addTextForm
from media.images import image
import os

INPUT = "Common_Event_Poster_Verticle_Withlogo.png"
OUTPUT = "static/text/result.png"
POSITION='bc'
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
    form= addTextForm(request.POST or None)
    if(request.method=='POST'):
        if form.is_valid():
            form.save()
            initial_obj = form.save(commit=False)
            initial_obj.save()
            # TODO
            # Create unique output file names
            # OUTPUT='static/result_'+request.POST['text']
            try:
                os.chdir('media/images')
                image.watermark_with_text(INPUT, OUTPUT, request.POST['text'], request.POST['position'])
                print('It worked')
            except Exception as e:
                print(e)
                print("Not working")
    context= {'form': form}
    return render(request,'text.html',context)


def viewAll(request):
    print(os.getcwd())
    list=os.listdir('static/text')
    for _ in range(len(list)):
        list[_] = "text/" + list[_]
    return render(request,'view.html',{'list':list})

