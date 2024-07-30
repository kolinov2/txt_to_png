import numpy as np
from PIL import Image

def image_to_bits(image_path):
    image = Image.open(image_path)
    rgb_values = np.array(image)

    bits = ''
    height, width, _ = rgb_values.shape

    for y in range(height):
        for x in range(width):
            r, g, b = rgb_values[y, x]
            # Convert RGB values to a 21-bit string (7 bits per channel)
            bit_chunk = f'{r:07b}{g:07b}{b:07b}'
            bits += bit_chunk

    return bits

def bits_to_text(bits):
    # Ensure the length of the bits is a multiple of 8
    padding_length = len(bits) % 8
    if padding_length != 0:
        bits = bits[:-padding_length]  # Remove extra bits

    # Split the bit string into 8-bit segments
    bytes_ = [bits[i:i + 8] for i in range(0, len(bits), 8)]

    # Convert bits to bytes
    byte_array = bytearray(int(b, 2) for b in bytes_)

    # Convert bytes to UTF-8 text
    text = byte_array.decode('utf-8', errors='ignore')

    return text

def main():
    image_file = 'output.png'  # Path to the PNG image file

    # Convert image to a bit string
    bits = image_to_bits(image_file)

    # Convert the bit string to UTF-8 text
    text = bits_to_text(bits)

    # Display the read text
    print('Read text:')
    print(text)

main()
