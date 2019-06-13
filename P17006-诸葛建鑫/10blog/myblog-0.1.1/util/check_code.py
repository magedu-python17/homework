import random
from PIL import Image, ImageFont, ImageDraw

# 验证码的基本字符
LOWERCASE = "abcdefghjkmnpqrstuvwxy"    # 去除干扰的i, l, o, z
UPPERCASE = LOWERCASE.upper()
NUM = "3456789"                         # 去除干扰的1， 2
INT_CHARS = "".join((LOWERCASE, UPPERCASE, NUM))

# 验证码图片信息
SIZE = (120, 30)


def gen_check_code(size=SIZE, chars=INT_CHARS, length=4, mode="RGB", bg_color=(255, 255, 255), font_color=(0, 0, 255),
                   font_size=24, font_type="simsun.ttc", draw_line=True, n_lines=(3, 4), draw_point=True,
                   chance_point=2):
    """
    :param size:        验证码图片大小, 格式(width, height)
    :param chars:       验证码中使用的字符集
    :param length:      每次生成的验证码图片中字符的数量
    :param mode:        图片的颜色模式
    :param bg_color:    图片的背景颜色
    :param font_color:  图片的字符颜色
    :param font_size:   验证码中字符的大小
    :param font_type:   图片中字符的字体类型(默认会从给定的路径加载字体类型，如果找不到，会去sys.path路径下查找是否有该文件)
    :param draw_line:   是否在验证码中添加干扰线条
    :param n_lines:     放置多少条干扰线，元组表示范围，只有draw_line=True时，才有效
    :param draw_point:  是否在验证码中添加干扰点
    :param chance_point:     干扰点出现的概率， 要求在[0, 100]
    :return:            一个图片实例以及验证码中的字符
    """
    width, height = size
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)

    def create_line():      # 绘制干扰线
        line_num = random.randint(*n_lines)
        for i in range(line_num):
            begin = (random.randint(0, width), random.randint(0, height))
            end = (random.randint(0, width), random.randint(0, height))
            draw.line([begin, end], fill=font_color)

    def create_point():     # 绘制干扰点
        chance = min(100, max(0, chance_point))     # 如果chance_point=2，表示图片中的像素点有2%的概率会被描绘有颜色的点
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp < chance:
                    draw.point((w, h), fill=font_color)

    def create_chars():
        s = random.sample(chars, length)
        new_s = " ".join(s)         # 在字符之间插入空格
        font = ImageFont.truetype(font_type, font_size)
        fw, fh = font.getsize(new_s)
        w, h = (width-fw)/2, (height-fh)/2
        draw.text((w, h), new_s, font=font, fill=font_color)
        return "".join(s)

    if draw_line:
        create_line()
    if draw_point:
        create_point()
    code = create_chars()
    return img, code

































































