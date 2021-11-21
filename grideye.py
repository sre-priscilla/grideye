import os
import sys
from string import digits, ascii_uppercase

from PIL import Image, ImageDraw, ImageFont, ImageOps


if __name__ == '__main__':
    image_file = sys.argv[1]
    scale = int(sys.argv[2])
    grid_size = int(sys.argv[3])

    # read image
    image = Image.open(image_file)
    width, height = image.size
    print(f'origin: width:{width}\theight:{height}')

    # resize image
    image = image.resize((width // scale, height // scale), Image.ANTIALIAS)
    width, height = image.size
    print(f'resize: width:{width}\theight:{height}')

    # expand border
    border_group = (
        grid_size,
        grid_size,
        grid_size-width % grid_size,
        grid_size-height % grid_size
    )
    image = ImageOps.expand(image, border=border_group, fill='white')
    width, height = image.size

    # draw line
    draw = ImageDraw.Draw(image)
    for i in range(0, width, grid_size):
        draw.line((i, 0, i, height), fill=0, width=1)
    for j in range(0, height, grid_size):
        draw.line((0, j, width, j), fill=0, width=1)

    # mark coordinate
    consolas = ImageFont.truetype('consolas.ttf', grid_size // 3)
    for i in range(0, width // grid_size):
        xy = ((i + 1) * grid_size, 0)
        draw.text(xy, ascii_uppercase[i], 0, font=consolas)
    for j in range(0, height // grid_size):
        xy = (0, (j + 1) * grid_size)
        draw.text(xy, digits[j], 0, font=consolas)

    image.show()