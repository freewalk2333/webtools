import base64

from PIL import Image, ImageDraw, ImageFont, ImageOps
from webtools.config.config import get_idcard_config
import datetime
import random
import os

simhei = r'C:/Windows/Fonts/simhei.ttf'
try:
    STXihei = r'C:/Windows/Fonts/STXihei.ttf'
except:
    STXihei = r'C:/Windows/Fonts/simhei.ttf'


def generate_idcard_frontside(name, idno, address):
    idcard_source_path = os.path.join(os.path.dirname(__file__), 'image/source/portrait.jpg').replace('\\', '/')
    idcard_save_path = os.path.join(os.path.dirname(__file__), 'image/target/').replace('\\', '/')
    image = Image.open(fp=idcard_source_path)
    draw = ImageDraw.Draw(im=image)
    name = list(name)
    id = list(idno)
    year = list(idno[6:10])
    month = list(str(int(idno[10:12])))
    day = list(idno[12:14])
    address = list(address)
    if int(str(idno[16:17])) % 2 == 1:
        sex = '男'
    else:
        sex = '女'
    namefont = ImageFont.truetype(font=simhei, size=36)
    sexfont = ImageFont.truetype(font=simhei, size=33)
    idfont = ImageFont.truetype(font=STXihei, size=38)
    birthfont = ImageFont.truetype(font=simhei, size=30)
    addressfont = ImageFont.truetype(font=simhei, size=34)
    # 注入姓名：
    for i in range(len(name)):
        draw.text(text=name[i], font=namefont, xy=(220 + i * 45, 101), fill=(0, 0, 0))
    # 注入性别：
    draw.text(text=sex, font=sexfont, xy=(220, 179), fill=(0, 0, 0))
    # 注入出生年份：
    for i in range(len(year)):
        draw.text(text=year[i], font=birthfont, xy=(220 + i * 15, 258), fill=(0, 0, 0))
    # 注入出生月份：
    for i in range(len(month)):
        draw.text(text=month[i], font=birthfont, xy=(375 + i * 15, 258), fill=(0, 0, 0))
    # 注入出生日期：
    for i in range(len(day)):
        draw.text(text=day[i], font=birthfont, xy=(463 + i * 15, 258), fill=(0, 0, 0))
    # 注入地址：
    for i in range(len(address)):
        draw.text(text=address[i], font=addressfont, xy=(220 + i * 37, 338), fill=(0, 0, 0))
    # 注入身份证号：
    for i in range(len(id)):
        draw.text(text=idno[i], font=idfont, xy=(373 + i * 30, 526), fill=(0, 0, 0))
    filename = str(idno) + '_' + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S' + '.png'))
    image.save(os.path.join(os.path.dirname(idcard_save_path), filename))
    with open(os.path.join(os.path.dirname(idcard_save_path), filename), 'rb') as file:
        image_base64_data = file.read()
        base64_str = base64.b64encode(image_base64_data).decode('utf-8')
        return 'data:image/png;base64,' + base64_str


def generate_hehei():
    image = Image.new('RGBA', (511, 318), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im=image)
    fontstyle = ImageFont.truetype(font=simhei, size=26)
    draw.text(text='图 片 在 此 展 示', font=fontstyle, xy=(145, 140), fill=(60, 60, 60))
    image.save('D:/AutomaticTest/IDcard/')


def generate_idcard_backside(date_start, date_end):
    fontstyle = ImageFont.truetype(font=simhei, size=55)
    idcard_source_path = os.path.join(os.path.dirname(__file__), 'image/source/emblem.png').replace('\\', '/')
    idcard_save_path = os.path.join(os.path.dirname(__file__), 'image/target/').replace('\\', '/')
    image = Image.open(fp=idcard_source_path)
    draw = ImageDraw.Draw(im=image)
    date = list(str(date_start[0:4] + '.' + str(date_start[5:7]) + '.' + str(date_start[8:10]) + '-' + str(
        date_end[0:4]) + '.' + str(date_end[5:7]) + '.' + str(date_end[8:10])))
    x = 678
    for i in range(len(date)):
        if date[i].isdigit():
            x += 13
            draw.text(text=date[i], font=fontstyle, xy=(x, 835), fill=(0, 0, 0))
            x += 14
        elif date[i] == '-':
            x += 16
            draw.text(text=date[i], font=fontstyle, xy=(x, 841), fill=(0, 0, 0))
            x += 16
        else:
            x += 13
            draw.text(text=date[i], font=fontstyle, xy=(x, 835), fill=(0, 0, 0))
            x += 2

    filename = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S' + '.png'))
    image.save(os.path.join(os.path.dirname(idcard_save_path), filename))
    with open(os.path.join(os.path.dirname(idcard_save_path), filename), 'rb') as file:
        image_base64_data = file.read()
        base64_str = base64.b64encode(image_base64_data).decode('utf-8')
        return 'data:image/png;base64,' + base64_str


if __name__ == '__main__':
    # print()
    # print(generate_idcard_frontside(name='张雷', idno='342623199810251234', address='北京市某个区某某某街道'))
    generate_idcard_backside('2015-08-14', '2025-08-14')
