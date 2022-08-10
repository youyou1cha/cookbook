# 为了kindle看漫画pdf,需要把jpg转成pdf

import os
from PIL import Image

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def pic2pdf(img_path,pdf_path):
    file_list = os.listdir(img_path)

    for x in file_list:
        if 'jpg' in x or 'png' in x or 'jpeg' in x:
            pdf_name = img_path.split('\\')[-2]
            im1 = Image.open(os.path.join(img_path,x))
            im1.save(pdf_path + pdf_name + '.pdf',"PDF",resolution=100.0)

if __name__ == '__main__':
    img_path = r'C:\Users\jojo\Documents\幽游白书\第1卷\\'
    pdf_path = r'C:\Users\jojo\Documents\幽游白书\第1卷\\'

    pic2pdf(img_path,pdf_path)