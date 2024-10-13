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

def text_h_center(axis, text, bottom, font_size):
    axis.text(WIDTH_4K / 2, bottom,
              text,
              fontproperties=noto_sans_sc['Regular'], fontsize=font_size,
              color='black', ha='center', va='center')

def code(axis, code, index):
    axis.text(LEFT_OFFSET, HEIGHT_4K - CONTENT_OFFSET - index * (MEDIUM_OFFSET + TINY_OFFSET + CONTENT_FONT_SIZE),
              code,
              fontproperties=noto_sans_sc['Light'], fontsize=CONTENT_FONT_SIZE,
              color='green', ha='left', va='top')

def headline(axis, headline, font_properties, fontsize, x_pos = WIDTH_4K / 2, y_pos = HEIGHT_4K / 2):
    # axis.axhline(y=HEIGHT_4K / 2, color='black', linewidth=1)
    # axis.axvline(x=WIDTH_4K / 2, color='black', linewidth=1)
    axis.text(x_pos, y_pos,
              headline,
              fontproperties=font_properties, fontsize=fontsize,
              ha='center', va='center',
              color='black')

def image_h_center(axis, image_path, bottom, scale=1, rotate=0):
    image = Image.open(image_path)
    image = image.rotate(rotate, expand=True)
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

def image_center(axis, image_path, pos_x, pos_y, scale=1, rotate=0):
    image = Image.open(image_path)
    image = image.rotate(rotate)
    image_width, image_height = image.width * scale, image.height * scale
    print('Image size', image_width, 'x', image_height)
    axis.imshow(image, extent=[pos_x - image_width / 2, pos_x + image_width / 2, pos_y - image_height / 2, pos_y + image_height / 2])

def image_2_h_center(axis, image1_path, image2_path, bottom, scale=1, margin_left=0):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    image1_width, image1_height = image1.width * scale, image1.height * scale
    print('Image size', image1_width, 'x', image1_height)
    image2_width, image2_height = image1.width * scale, image2.height * scale
    print('Image size', image2_width, 'x', image2_height)
    image1_left_offset = (WIDTH_4K - margin_left - (image1_width + image2_width)) // 3
    image2_left_offset = image1_left_offset * 2 + image1_width
    axis.imshow(image1, extent=[margin_left + image1_left_offset, margin_left + image1_left_offset + image1_width, bottom, bottom + image1_height])
    axis.imshow(image2, extent=[margin_left + image2_left_offset, margin_left + image2_left_offset + image2_width, bottom, bottom + image2_height])

def image_by_offset(axis, image_path, left, bottom, scale=1):
    image = Image.open(image_path)
    image_width, image_height = image.width * scale, image.height * scale
    print('Image size', image_width, 'x', image_height)
    axis.imshow(image, extent=[left, left + image_width, bottom, bottom + image_height])

def save(file_path):
    temp_dir = 'temp'
    file_path = os.path.join(temp_dir, file_path)
    pyplot.savefig(file_path, dpi=DPI, bbox_inches='tight', pad_inches=0, transparent=False)
