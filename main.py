from PIL import Image
import numpy as np
import sys

def text_to_bin(text):
    binary = ''.join(format(byte, '08b') for byte in text.encode('utf-8'))
    return binary

def bin_to_text(binary):
    byte_array = bytearray(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))
    return byte_array.decode('utf-8', errors='ignore')

def encode_image(image_path, secret_message):
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image, dtype=np.uint8)
    binary_message = text_to_bin(secret_message) + '1111111111111110'  # Stop marker
    
    # Check if image has enough capacity
    max_capacity = pixels.size // 3  # Each RGB pixel can store 3 bits
    if len(binary_message) > max_capacity:
        print("Error: Message is too long for this image.")
        sys.exit(1)
    
    binary_index = 0
    for row in pixels:
        for pixel in row:
            for i in range(3):  # RGB channels
                if binary_index < len(binary_message):
                    pixel[i] = (pixel[i] & 0b11111110) | int(binary_message[binary_index])
                    binary_index += 1
                else:
                    break
    
    encoded_image = Image.fromarray(pixels)
    
    print("Choose output format:")
    print("1. PNG")
    print("2. BMP")
    print("3. TIFF")
    print("4. JPEG (Not recommended due to compression artifacts)")
    choice = input("Enter choice (1/2/3/4): ")
    
    format_map = {"1": "png", "2": "bmp", "3": "tiff", "4": "jpg"}
    output_format = format_map.get(choice, "png")  # Default to PNG if invalid choice
    output_path = f"output.{output_format}"
    
    if output_format == "jpg":
        print("Warning: JPEG compression may corrupt hidden data! Use PNG, BMP, or TIFF instead.")
        temp_output = "output.png"  # Save as PNG first
        encoded_image.save(temp_output, format="PNG")
        Image.open(temp_output).convert("RGB").save(output_path, format="JPEG", quality=100, subsampling=0)
    else:
        encoded_image.save(output_path, format=output_format.upper())
    
    print(f"Message hidden successfully in {output_path}!")

def decode_image(image_path):
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image, dtype=np.uint8)
    binary_message = ''
    
    for row in pixels:
        for pixel in row:
            for i in range(3):
                binary_message += str(pixel[i] & 1)
                if binary_message[-16:] == '1111111111111110':  # Stop marker
                    return bin_to_text(binary_message[:-16])
    
    return bin_to_text(binary_message)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <encode/decode> <image_path> [message]")
        sys.exit(1)
    
    mode = sys.argv[1]
    image_path = sys.argv[2]
    
    if mode == "encode":
        if len(sys.argv) < 4:
            print("Usage: python script.py encode <image_path> <message>")
            sys.exit(1)
        message = sys.argv[3]
        encode_image(image_path, message)
    elif mode == "decode":
        print("Hidden message:", decode_image(image_path))
    else:
        print("Invalid mode! Use 'encode' or 'decode'.")
