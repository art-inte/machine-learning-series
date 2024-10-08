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

def image(axis, image_path, bottom):
    image = Image.open(image_path)
    image_width, image_height = image.width, image.height
    print('Image size', image_width, 'x', image_height)
    left_offset = (WIDTH_4K - image_width) / 2
    axis.imshow(image, extent=[left_offset, left_offset + image_width, bottom, bottom + image_height])

def save(file_path):
    pyplot.savefig(file_path, dpi=DPI, bbox_inches='tight', pad_inches=0, transparent=False)
