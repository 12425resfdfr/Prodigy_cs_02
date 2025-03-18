from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Encrypt the image by swapping pixel values and applying XOR operation
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Swap red and blue channels
            r, b = b, r

            # Apply XOR operation with the key
            r ^= key
            g ^= key
            b ^= key

            # Update the pixel with the new values
            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    encrypted_image_path = image_path.replace(".png", "_encrypted.png")
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Decrypt the image by reversing the operations
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Apply XOR operation with the key (reverse the encryption)
            r ^= key
            g ^= key
            b ^= key

            # Swap red and blue channels back to original
            r, b = b, r

            # Update the pixel with the original values
            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    decrypted_image_path = encrypted_image_path.replace("_encrypted.png", "_decrypted.png")
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

def main():
    # Ask the user for the image path and encryption key
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption key (an integer): "))

    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the image
    encrypted_image_path = image_path.replace(".png", "_encrypted.png")
    decrypt_image(encrypted_image_path, key)

if __name__ == "__main__":
    main()