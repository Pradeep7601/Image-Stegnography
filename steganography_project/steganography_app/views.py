# steganography_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image


def home(request):
    return render(request, 'home.html')


def encode(request):
    if request.method == 'POST':
        # Get the input image and text from the form
        image = request.FILES['image']
        text = request.POST['text']

        # Open the image using Pillow
        with Image.open(image) as img:
            # Convert text to binary
            binary_text = ''.join(format(ord(char), '08b') for char in text)

            # Add the length of the binary text to the beginning (32 bits)
            binary_text = format(len(binary_text), '032b') + binary_text

            # Flatten the binary text and image pixels
            pixels = list(img.getdata())
            pixels = [list(pixel) for pixel in pixels]

            # Embed the binary text into the least significant bit of each pixel
            for i in range(len(binary_text)):
                pixels[i] = list(pixels[i])
                pixels[i][-1] = int(binary_text[i])

            # Create a new image with the embedded text
            encoded_image = Image.new(img.mode, img.size)
            encoded_image.putdata([tuple(pixel) for pixel in pixels])

            # Save the encoded image
            encoded_image.save('encoded_image.png')

        return HttpResponse('Image encoded and saved successfully!')

    return render(request, 'encode.html')


def decode(request):
    if request.method == 'POST':
        # Get the input image from the form
        image = request.FILES['image']

        try:
            # Open the image using Pillow
            with Image.open(image) as img:
                # Extract the binary message from the image
                binary_text = ''
                pixels = list(img.getdata())

                for pixel in pixels:
                    # Extract the least significant bit from the last channel
                    channel = pixel[-1]
                    binary_text += str(channel)

                # Convert binary text to ASCII
                decoded_text = ''
                for i in range(0, len(binary_text), 8):
                    byte = binary_text[i:i+8]
                    try:
                        decoded_text += chr(int(byte, 2))
                    except ValueError:
                        break  # Break if there is an issue decoding the byte

                return HttpResponse(f'Decoded Message: {decoded_text.strip()}')
        except Exception as e:
            return HttpResponse(f'Error decoding: {e}')

    return render(request, 'decode.html')
