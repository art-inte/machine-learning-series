import matplotlib.pyplot as pyplot
from config import *
from PIL import Image

def init(color='white'):
    figure, axis = pyplot.subplots(figsize=(WIDTH_4K / DPI, HEIGHT_4K / DPI), dpi=DPI)
    axis.set_xlim(0, WIDTH_4K)
    axis.set_ylim(0, HEIGHT_4K)
    figure.patch.set_facecolor(color)
    axis.set_facecolor(color)
    axis.axis('off')
    # 绘制网格线
    return figure, axis

def title(axis, title):
    axis.text(LEFT_OFFSET, HEIGHT_4K - TITLE_OFFSET,
              title,
              fontproperties=noto_sans_sc['Bold'], fontsize=TITLE_FONT_SIZE,
              color='black', ha='left', va='top')

def subtitle(axis, subtitle):
    axis.text(LEFT_OFFSET, HEIGHT_4K - SUBTITLE_OFFSET,
              subtitle,
              fontproperties=noto_sans_sc['Medium'], fontsize=SUBTITLE_FONT_SIZE,
              color='black', ha='left', va='top')

def text(axis, text, index):
    axis.text(LEFT_OFFSET, HEIGHT_4K - CONTENT_OFFSET - index * (MEDIUM_OFFSET + TINY_OFFSET + CONTENT_FONT_SIZE),
              text,
              fontproperties=noto_sans_sc['Regular'], fontsize=CONTENT_FONT_SIZE,
              color='black', ha='left', va='top')

def code(axis, code, index):
    axis.text(LEFT_OFFSET, HEIGHT_4K - CONTENT_OFFSET - index * (MEDIUM_OFFSET + TINY_OFFSET + CONTENT_FONT_SIZE),
              code,
              fontproperties=noto_sans_sc['Light'], fontsize=CONTENT_FONT_SIZE,
              color='green', ha='left', va='top')

def headline(axis, headline, font_properties, fontsize, x_pos = WIDTH_4K / 2, y_pos = HEIGHT_4K / 2):
    axis.text(x_pos, y_pos,
              headline,
              fontproperties=font_properties, fontsize=fontsize,
              ha='center', va='center',
              color='black')

def image_h_center(axis, image_path, bottom, scale=1):
    image = Image.open(image_path)
    image_width, image_height = image.width * scale, image.height * scale
    print('Image size', image_width, 'x', image_height)
    left_offset = (WIDTH_4K - image_width) / 2
    axis.imshow(image, extent=[left_offset, left_offset + image_width, bottom, bottom + image_height])

def image_v_center(axis, image_path, left, scale=1):
    image = Image.open(image_path)
    image_width, image_height = image.width * scale, image.height * scale
    print('Image size', image_width, 'x', image_height)
    bottom_offset = (HEIGHT_4K - image_height) / 2
    axis.imshow(image, extent=[left, left + image_width, bottom_offset, bottom_offset + image_height])

def image_2_h_center(axis, image1_path, image2_path, bottom, scale=1):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    if image1.width != image2.width or image1.height != image2.height:
        print('Size image1', image1.width, 'x', image1.height)
        print('Size image2', image2.width, 'x', image2.height)
        return
    image_width, image_height = image1.width * scale, image2.height * scale
    image1_left_offset = (WIDTH_4K - 2 * image_width) // 3
    image2_left_offset = image1_left_offset * 2 + image_width
    axis.imshow(image1, extent=[image1_left_offset, image1_left_offset + image_width, bottom, bottom + image_height])
    axis.imshow(image2, extent=[image2_left_offset, image2_left_offset + image_width, bottom, bottom + image_height])

def image_by_offset(axis, image_path, left, bottom, scale=1):
    image = Image.open(image_path)
    image_width, image_height = image.width * scale, image.height * scale
    print('Image size', image_width, 'x', image_height)
    axis.imshow(image, extent=[left, left + image_width, bottom, bottom + image_height])

def save(file_path):
    pyplot.savefig(file_path, dpi=DPI, bbox_inches='tight', pad_inches=0, transparent=False)
