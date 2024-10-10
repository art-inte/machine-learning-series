import os
from matplotlib import font_manager

WIDTH_4K = 3840
HEIGHT_4K = 2160
DPI = 100

TINY_OFFSET = 12
SMALL_OFFSET = 24
MEDIUM_OFFSET = 48
LARGE_OFFSET = 96
EXTRA_OFFSET = 192
ULTRA_OFFSET = 384

TINY_SIZE = 12
SMALL_SIZE = 24
MEDIUM_SIZE = 48
LARGE_SIZE = 96
EXTRA_SIZE = 192
ULTRA_SIZE = 384

LEFT_OFFSET = 128
RIGHT_OFFSET = 128

# font size
TITLE_FONT_SIZE = 64
SUBTITLE_FONT_SIZE = 52
CONTENT_FONT_SIZE = 40

TITLE_OFFSET = 128
SUBTITLE_OFFSET = TITLE_OFFSET + TITLE_FONT_SIZE + LARGE_OFFSET
CONTENT_OFFSET = SUBTITLE_OFFSET + SUBTITLE_FONT_SIZE + LARGE_OFFSET

YOUTUBE_COVER_DEFAULT_WIDTH = 2560
YOUTUBE_COVER_DEFAULT_HEIGHT = 1440

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
