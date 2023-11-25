# Image-Stegnography
Image steganography is a technique used to hide information within an image without changing its perceptual quality significantly. The Least Significant Bit (LSB) method is one of the simplest and widely used techniques in steganography. In this method, information is embedded in the least significant bit of each pixel in the image.

**Process:**

**Binary Representation:**
In digital images, each pixel is represented by color channels (RGB for most images). Each channel has a pixel value ranging from 0 to 255. In binary, this is an 8-bit representation.
Convert Message to Binary:
The message (text, for example) to be hidden is converted into binary format. This is often done by representing each character in the ASCII table as an 8-bit binary number.

**Embedding:**
For each pixel in the image, the least significant bit (LSB) of each color channel is replaced with a bit from the binary message.
For example, if the pixel has an original binary representation of 10110110 and the message bit to be embedded is 1, the modified binary representation becomes 10110111.

**Hidden Data Capacity:**
The LSB method allows hiding one bit of information in each color channel for every pixel. This means that for an RGB image, three bits (one in each channel) can be used per pixel.

**Encoding Example:**
Suppose we have the pixel (R=11001011, G=10110100, B=01011101) and we want to hide the message 0101. After encoding, the pixel becomes (R=11001010, G=10110101, B=01011100).

**Decoding:**
To extract the hidden message, one simply needs to read the LSB of each color channel in each pixel and concatenate them to form the binary message.
For the example above, the hidden message would be 0101.
