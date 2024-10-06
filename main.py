import sys
import numpy as np
from PIL import Image, ImageOps

value_to_character_map = '█$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\' '[::-1]


def image_to_text(image: np.ndarray) -> str:
    text = ''
    for i in range(image.shape[0]):
        for k in range(image.shape[1]):
            greyscale_value = image[i][k]
            text += value_to_character_map[int(
                (len(value_to_character_map) - 1) * (greyscale_value / 255))]
        text += '\n'
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
    print(image_as_text)


if __name__ == '__main__':
    main()
