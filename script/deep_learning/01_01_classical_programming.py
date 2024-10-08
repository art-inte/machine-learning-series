import matplotlib.pyplot as pyplot
from PIL import Image
from config import *

if __name__ == '__main__':
    figure, axis = pyplot.subplots(figsize=(WIDTH_4K / DPI, HEIGHT_4K / DPI), dpi=DPI)
    axis.set_xlim(0, WIDTH_4K)
    axis.set_ylim(0, HEIGHT_4K)
    figure.patch.set_facecolor('white')
    axis.set_facecolor('white')
    axis.axis('off')

    axis.text(TITLE_OFFSET, HEIGHT_4K - TITLE_OFFSET,
              '01-机器学习与深度学习介绍',
              fontproperties=noto_sans_sc['Bold'], fontsize=TITLE_FONT_SIZE,
              color='black', ha='left', va='top')
    axis.text(TITLE_OFFSET, HEIGHT_4K - (TITLE_OFFSET + TITLE_FONT_SIZE * 3),
              '1.1 传统编程',
              fontproperties=noto_sans_sc['Medium'], fontsize=SUBTITLE_FONT_SIZE,
              color='black', ha='left', va='top')
    axis.text(TITLE_OFFSET, HEIGHT_4K - (TITLE_OFFSET + TITLE_FONT_SIZE * 5),
              '规则',
              fontproperties=noto_sans_sc['Light'], fontsize=CONTENT_FONT_SIZE,
              color='black', ha='left', va='top')
    pyplot.savefig('01_01_classical_programming.png', dpi = DPI, bbox_inches='tight', pad_inches=0, transparent=False)
