from django import forms

from .models import Images



class ImageForm(forms.ModelForm):
    class Meta:
        model= Images
        fields= ["text", "position","logo"]
# try:
# 				os.chdir('C:/Users/pc/Desktop/Social- share/socialShare/media/images')
# 				print(os.getcwd())
# 				cmd='cmd /c "python main.py'+' '+logo+'"'
# 				print(cmd)
# 				os.system('cmd /c "python main.py"')
# 				print('It worked')
# 			except Exception as e:
# 				print(e)
# 				print("Not working")