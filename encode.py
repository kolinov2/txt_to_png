import numpy as np
from PIL import Image
import math
import os


def text_to_bits(text):
    """Converts UTF-8 text to a bit string."""
    bits = ''.join(f'{byte:08b}' for byte in text.encode('utf-8'))
    return bits


def calculate_dimensions(total_bits):
    """Calculates the dimensions of a rectangular image based on the available bits."""
    num_pixels = total_bits // 21  # 21 bits per pixel (7 bits per RGB channel)
    width = int(math.ceil(math.sqrt(num_pixels)))
    height = int(math.ceil(num_pixels / width))

    # The image dimensions must fit exactly the number of pixels
    while width * height < num_pixels:
        width += 1
        height = int(math.ceil(num_pixels / width))

    return width, height


def bits_to_rgb(bits, width, height):
    """Converts a bit string to an RGB array with dimensions width x height."""
    num_pixels = width * height
    rgb_values = np.zeros((height, width, 3), dtype=np.uint8)

    # Add padding if necessary
    bits = bits.ljust(num_pixels * 21, '0')

    for i in range(num_pixels):
        start = i * 21
        end = start + 21
        bit_chunk = bits[start:end]

        # Split bit_chunk into three RGB parts
        r = int(bit_chunk[:7], 2)
        g = int(bit_chunk[7:14], 2)
        b = int(bit_chunk[14:], 2)

        # Set RGB values
        y, x = divmod(i, width)
        rgb_values[y, x] = [r, g, b]

    return rgb_values


def create_png_image(rgb_values, output_file):
    """Creates a PNG image from an RGB array."""
    image = Image.fromarray(rgb_values, 'RGB')
    image.save(output_file)


def main():
    txt_file = 'input.txt'  # Path to the text file
    output_image = 'output.png'

    # Convert text file to bit string
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()
    bits = text_to_bits(text)

    # Calculate the number of available pixels and the image dimensions
    total_bits = len(bits)
    width, height = calculate_dimensions(total_bits)

    # Convert bit string to RGB array
    rgb_values = bits_to_rgb(bits, width, height)

    # Create PNG image
    create_png_image(rgb_values, output_image)

    # Get image resolution and file size
    image = Image.open(output_image)
    img_width, img_height = image.size
    file_size = os.path.getsize(output_image) / 1024  # size in KB

    print(f'Done! Image resolution: {img_width}x{img_height}')
    print(f'File size: {file_size:.2f} KB')


main()
