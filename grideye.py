import sys

from PIL import Image, ImageDraw


if __name__ == '__main__':
    image_file = sys.argv[1]
    grid_size = int(sys.argv[2])

    image = Image.open(image_file)
    width, height = image.size

    draw = ImageDraw.Draw(image)
    for x in range(0, width, grid_size):
        draw.line((x, 0, x, height), fill=128, width=5)
    for y in range(0, height, grid_size):
        draw.line((0, y, width, y), fill=128, width=5)

    image.show()
