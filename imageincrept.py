from PIL import Image
import random

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")

    pixels = list(img.getdata())

    random.seed(key)

    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]

    random.shuffle(encrypted_pixels)

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)

    encrypted_img.save(output_path)
    print(f"Image encrypted successfully: {output_path}")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")

    pixels = list(img.getdata())

    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)

    decrypted_pixels = [None] * len(pixels)
    for i, idx in enumerate(indices):
        decrypted_pixels[idx] = pixels[i]

    decrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in decrypted_pixels]

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)

    decrypted_img.save(output_path)
    print(f"Image decrypted successfully: {output_path}")


if __name__ == "__main__":
    print("=== Image Encryption & Decryption Tool ===")

    choice = input("Enter E for Encrypt or D for Decrypt: ").lower()

    try:
        key = int(input("Enter Secret Key (number): "))
    except ValueError:
        print("Key must be a number!")
        exit()

    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path (use .png): ")

    if choice == "e":
        encrypt_image(input_path, output_path, key)
    elif choice == "d":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice! Use E or D only.")