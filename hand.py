from PIL import Image, ImageDraw, ImageFont
import textwrap
import os




def draw_multiple_line_text(image, text, font, text_color, text_start_height,num):
    
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    
    lines = textwrap.wrap(text, width=65)
    
    for line in lines:
        line_width, line_height = font.getsize(line)
        
        draw.text((10, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height
        if y_text+line_height > 800:
            save_img(num,image)
            num += 1

            # image.save('img/pil_text'+str(num)+'.png')
            write(' '.join(lines[lines.index(line)+1:]),num)
            # write(' '.join(lines[lines.index(line):]),num+1)
            break

    save_img(num,image)

total_pages = 0
def save_img(num,image):
    global total_pages
    total_pages = max(total_pages,num)
    
    image.save('page'+str(num)+'.png')

def write(txt,num):
    image = Image.new('RGB', (600, 800), color = (197,189,186))
    fontsize = 18  # starting font size
    font = ImageFont.truetype("khand.ttf", fontsize)
    

    text_color = (0,0,150)
    text_start_height = 0
    num = draw_multiple_line_text(image, txt, font, text_color, text_start_height,num)

    
    # draw_multiple_line_text(image, text2, font, text_color, 400)
    

def begin_writing():
    '''
    Testing draw_multiple_line_text
    '''
    with open('text/assignment1.txt','rb') as f:
        txt = f.read().decode('latin-1')
    write(txt,0)
    print(total_pages)
    img1 = Image.open('page0.png')
    im_list = [Image.open('page{}.png'.format(i)) for i in range(1,total_pages+1)]
    img1.save('./handwritten.pdf', "PDF", resolution=200.0, save_all=True, append_images=im_list)

    for i in range(total_pages+1):
        os.remove('page{}.png'.format(i))
    # os.remove('./handwritten.pdf')
    #image_width

begin_writing()
    
