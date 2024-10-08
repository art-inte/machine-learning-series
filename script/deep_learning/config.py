import os
from matplotlib import font_manager

WIDTH_4K = 3840
HEIGHT_4K = 2160
DPI = 100

TITLE_OFFSET = 128

# font size
TITLE_FONT_SIZE = 64
SUBTITLE_FONT_SIZE = 48
CONTENT_FONT_SIZE = 36

# google font path
# Download from url: https://fonts.google.com/noto/specimen/Noto+Sans+SC?lang=zh_Hans
BASE_FONT_PATH = '/Users/admin/github/machine-learning-series/temp/Noto_Sans_SC/static'

NOTO_SANS_SC_FAMILY = [
    'NotoSansSC-Thin.ttf',
    'NotoSansSC-ExtraLight.ttf',
    'NotoSansSC-Light.ttf',
    'NotoSansSC-Regular.ttf',
    'NotoSansSC-Medium.ttf',
    'NotoSansSC-SemiBold.ttf',
    'NotoSansSC-Bold.ttf',
    'NotoSansSC-ExtraBold.ttf',
    'NotoSansSC-Black.ttf',
]
noto_sans_sc = {}
for font_name in NOTO_SANS_SC_FAMILY:
    font_path = os.path.join(BASE_FONT_PATH, font_name)
    property_name = font_name.removeprefix('NotoSansSC-').removesuffix('.ttf')
    noto_sans_sc[property_name] = font_manager.FontProperties(fname=font_path)
