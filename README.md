# Text to PNG Converter
![bannerotp](https://github.com/user-attachments/assets/77e6b7e0-dcef-4f0c-84d6-6e549bb26f9e)

This project provides a Python script that converts a UTF-8 encoded text file into a PNG image, where each pixel represents a portion of the text encoded in RGB color values. The image is created with the exact dimensions required to fully encode the text, and any excess bits are padded with black pixels.

## Features

- Converts UTF-8 text to a bit string.
- Encodes the bit string into an RGB PNG image.
- Provides information about image resolution and file size after creation.

## Requirements

To run this project, you need to have the following Python libraries installed:

- `numpy`
- `Pillow` (PIL fork)

You can install these libraries using pip:

```bash
pip install pip install -r requirements.txt
```
## How to use

#### If you want to encode:
1. edit input.txt file
2. run ```encode.py```
3. output.png will be created

#### If you want to decode:
1. run  ```decode.py```


## How Text Encoding and Decoding Work

### Encoding Text to PNG Image

1. **Convert Text to Bits**:
   - UTF-8 text is converted into a string of bits. Each character is encoded into 8 bits (1 byte), and the entire text is transformed into one long bit string.

2. **Convert Bits to RGB Values**:
   - The long bit string is split into 21-bit segments. Each segment is divided into three parts: 7 bits for the red (R) channel, 7 bits for the green (G) channel, and 7 bits for the blue (B) channel.
   - These values are then converted into integers (0-127) and assigned to the corresponding pixels in the image.

3. **Create and Save PNG Image**:
   - An RGB image is created from the RGB values and saved as a PNG file. Each pixel corresponds to a bit segment encoding part of the text.

### Decoding PNG Image to Text

1. **Read PNG Image**:
   - The PNG image is opened and read as an RGB array. Each pixel contains RGB values that were used to encode the text.

2. **Convert RGB Values to Bits**:
   - The RGB values of each pixel are converted back into a bit string. 7 bits from each RGB channel are combined to form a 21-bit segment.

3. **Reconstruct Text from Bits**:
   - The resulting bit string is split into 8-bit segments, which are then converted back into bytes.
   - The bytes are used to reconstruct the text in UTF-8 format.

## Example

| Txt File       | Image    | Resolution   |
|----------------|----------------|----------------|
|[loremipsum.txt](example_txt/loremipsum.txt)|![output](https://github.com/user-attachments/assets/26088b05-0f25-4b7e-bd1b-7459550c795b)| 48x48 |
|[utf8-test.txt](example_txt/utf8-test.txt)  |![output](https://github.com/user-attachments/assets/9feec1cd-a3d1-4d3f-b6a4-5e8938feca24)| 72X72 |

#### by kolino :)

