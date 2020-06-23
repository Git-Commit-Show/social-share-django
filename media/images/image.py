from PIL import Image, ImageDraw, ImageFont
import os

# DEAFULTS

INPUT = "Common_Event_Poster_Verticle_Withlogo.png"
OUTPUT = "output/result.png"
POSITION='bcl'
DISPLAY = False
TEXT = ""                               # Let it be empty unless you want text and watermark both
FONT = "fonts/Helvetica.ttf"
COLOR = "white"
TEXT_SIZE = 40
TEXT_POSITION = "bc"
TEXT_ALIGN_WATERMARK = "r"              # Text Position wrt Watermark


def watermark(
              input_image_path,
              output_image_path,
              watermark_image_path,
              position_logo,
              text=TEXT,
              color=COLOR,
              text_size=TEXT_SIZE,
              text_position=TEXT_ALIGN_WATERMARK
              ):

    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert('RGBA')
    SIZE = 300,150
    watermark.thumbnail((SIZE),resample=0)
    width_base, height_base = base_image.size
    width_water, height_water = watermark.size

    transparent = Image.new('RGB', (width_base, height_base))

    transparent.paste(base_image, (0,0))
    bias_width=int(width_base*.03)
    bias_height=int(height_base*.03)

    mapper_logo_position={'tl':(bias_width,bias_height),
            'tc':(width_base//2-width_water//2,bias_height),
            'tr':(width_base-width_water-bias_width,bias_height),
            'cl':(bias_width,height_base//2-height_water),
            'cr':(width_base-width_water-bias_width,height_base//2-height_water),
            'c':(width_base//2-width_water//2,height_base//2-height_water),
            'bl':(bias_width,height_base-height_water-bias_height), #
            'bc':(width_base//2-width_water//2,height_base-height_water-bias_height),
            'bcl':(int(width_base/2.2)-width_water//2,height_base-height_water-bias_height),
            'br':(width_base-width_water-bias_width,height_base-height_water-bias_height)}

    transparent.paste(watermark, mapper_logo_position[position_logo], mask=watermark)
    drawing = ImageDraw.Draw(transparent)
    #drawing = Image.new('RGB',transparent.size,(255,255,255,255))

    font = ImageFont.truetype(FONT, text_size)
    textwidth, textheight = drawing.textsize(text, font)
    mapper_text_position={
        'r':(mapper_logo_position[position_logo][0]+width_water+bias_width//2,mapper_logo_position[position_logo][1]+height_water//2-textheight//2),
        'b':[mapper_logo_position[position_logo][0]+width_water//2-textwidth//2,mapper_logo_position[position_logo][1]+height_water+bias_width//2]
    }
    position_text=mapper_text_position[text_position]
    if(textwidth<width_water):
        mapper_text_position['b'][0]=mapper_logo_position[position_logo][0]+(width_water-textwidth)//2
    drawing.text(position_text, text, fill=color,font=font)
    if DISPLAY:
        transparent.show()
    transparent.save(output_image_path)


def watermark_with_text(input_image_path,
                        output_image_path,
                        text=TEXT,
                        text_position=TEXT_POSITION,
                        color=COLOR,
                        text_size=TEXT_SIZE,
                       ):

    base_image = Image.open(input_image_path) 
    width_base, height_base = base_image.size 

    drawing = ImageDraw.Draw(base_image)
    bias_width=int(width_base*.05)
    bias_height=int(height_base*.05)
    if bias_height>50:
        bias_height=50
    if bias_width>50:
        bias_width=50

    font = ImageFont.truetype(FONT, text_size)
    textwidth, textheight = drawing.textsize(text, font)
    mapper_position={'tl':(bias_width,bias_height),
            'tc':(width_base//2-textwidth//2,bias_height),
            'tr':(width_base-textwidth-bias_width,bias_height),
            'cl':(bias_width,height_base//2-textheight),
            'cr':(width_base-textwidth-bias_width,height_base//2-textheight),
            'c':(width_base//2-textwidth//2,height_base//2-textheight),
            'bl':(bias_width,height_base-textheight-bias_height),
            'bc':(width_base//2-textwidth//2,height_base-textheight-bias_height),
            'br':(width_base-textwidth-bias_width,height_base-textheight-bias_height)}


    drawing.text(mapper_position[text_position], text,fill=color, font=font) 
    if DISPLAY:
        base_image.show()
    base_image.save(output_image_path)

def watermark_a_folder(folder_path):
    global OUTPUT
    logo_list=os.listdir(folder_path)
    for i in logo_list:
        OUTPUT=OUTPUT+'result'+'_'+i
        watermark(INPUT,OUTPUT,folder_path+i,POSITION)
        OUTPUT = "output/"
    
