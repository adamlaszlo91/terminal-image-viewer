import sys
import numpy as np
from PIL import Image, ImageOps


def image_to_text(image: np.ndarray) -> str:
    text = ''
    for i in range(image.shape[0]):
        for k in range(image.shape[1]):
            text += "█" if image[i][k] > 0 else ' '
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

    image = image.convert('1')
    image = ImageOps.contain(image, (80, 80))
    image = image.resize((80, image.height // 2))
    image_array = np.asarray(image)

    image_as_text = image_to_text(image_array)
    print(image_as_text)


if __name__ == '__main__':
    main()
