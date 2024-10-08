import sys
import numpy as np
from PIL import Image, ImageOps

ascii_chars = '█$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\' '[::-1]


def image_to_text(image: np.ndarray) -> str:
    text = ''
    for i in range(image.shape[0]):
        text += '\n'
        for k in range(image.shape[1]):
            greyscale_value = image[i][k]
            char_index = int((greyscale_value / 256) * (len(ascii_chars) ))
            text += ascii_chars[char_index]
    return text


def main() -> None:
    if len(sys.argv) < 2:
        print('Please provide the image path.')
        return

    try:
        image = Image.open(sys.argv[1])
    except:
        print('Please provide a valid image path.')
        return

    image = image.convert('L')
    image = ImageOps.contain(image, (80, 80))
    image = image.resize((80, image.height // 2))
    image_array = np.asarray(image)

    image_as_text = image_to_text(image_array)
    print(image_as_text, flush=True)


if __name__ == '__main__':
    main()
