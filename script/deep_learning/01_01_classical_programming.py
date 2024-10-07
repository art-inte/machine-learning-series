import matplotlib.pyplot as pyplot
from matplotlib import font_manager
from PIL import Image

WIDTH_4K = 3840
HEIGHT_4K = 2160
DPI = 100

TITLE_OFFSET = 128
TITLE_FONT_SIZE = 64
SUBTITLE_FONT_SIZE = 48
CONTENT_FONT_SIZE = 36

# TODO: Download from url: https://fonts.google.com/selection?lang=zh_Hans
FONT_MEDIUM_PATH = '/Users/wangrl/Downloads/Noto_Sans_SC/static/NotoSansSC-Medium.ttf'
FONT_REGULAR_PATH = '/Users/wangrl/Downloads/Noto_Sans_SC/static/NotoSansSC-Regular.ttf'
FONT_LIGHT_PATH = '/Users/wangrl/Downloads/Noto_Sans_SC/static/NotoSansSC-Light.ttf'

if __name__ == '__main__':
    font_medium_prop = font_manager.FontProperties(fname=FONT_MEDIUM_PATH)
    font_regular_prop = font_manager.FontProperties(fname=FONT_REGULAR_PATH)
    font_light_prop =  font_manager.FontProperties(fname=FONT_LIGHT_PATH)
    figure, axis = pyplot.subplots(figsize=(WIDTH_4K / DPI, HEIGHT_4K / DPI), dpi=DPI)
    axis.set_xlim(0, WIDTH_4K)
    axis.set_ylim(0, HEIGHT_4K)
    figure.patch.set_facecolor('white')
    axis.set_facecolor('white')
    axis.axis('off')

    axis.text(TITLE_OFFSET, HEIGHT_4K - TITLE_OFFSET,
              '01-机器学习与深度学习介绍',
              fontproperties=font_medium_prop, fontsize=TITLE_FONT_SIZE,
              color='black', ha='left', va='top')
    axis.text(TITLE_OFFSET, HEIGHT_4K - (TITLE_OFFSET + TITLE_FONT_SIZE * 3),
              '1.3 传统编程',
              fontproperties=font_regular_prop, fontsize=SUBTITLE_FONT_SIZE,
              color='black', ha='left', va='top')
    axis.text(TITLE_OFFSET, HEIGHT_4K - (TITLE_OFFSET + TITLE_FONT_SIZE * 5),
              "def check_loan_eligibility(age, income):\n    if age < 18 or age > 65:\n        return 'NO'\n    if income < 30000:\n        return 'NO'\n    return 'YES'",
              fontproperties=font_regular_prop, fontsize=CONTENT_FONT_SIZE,
              color='black', ha='left', va='top')
    pyplot.savefig('01_01_classical_programming.png', dpi = DPI, bbox_inches='tight', pad_inches=0, transparent=False)