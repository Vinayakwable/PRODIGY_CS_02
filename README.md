🔐 Image Encryption & Decryption Tool (Python)

📌 Project Overview

This project is a basic image encryption and decryption tool built using Python and the Pillow library. It uses simple techniques like XOR operation and pixel shuffling to obfuscate image data for learning purposes.

> ⚠️ This is an educational project, not a secure cryptographic system.


🧠 Objective

To understand:

How digital images store pixel data

How XOR works in data transformation

How shuffling affects data integrity

Basics of building security-related Python tools

⚙️ Features

Encrypt any image using a numeric secret key
Decrypt the image using the same key
Supports common formats like PNG and JPG
Uses RGB pixel manipulation

🛠️ Technologies Used

Python
Pillow (PIL)
Random module

📂 How It Works

1. Loads the image and converts it to RGB
2. Applies XOR operation to each pixel using a key
3. Randomly shuffles pixel positions based on the same key
4. Decryption reverses the shuffle and XOR process

▶️ How to Run

pip install pillow
python image_encryptor.py
You will be prompted to:
Choose Encrypt or Decrypt
Enter secret key
Provide input image path
Provide output image path

📸 Example

Original Image → Encrypted Image → Decrypted Image

🚧 Limitations
Not real encryption (vulnerable to attacks)

Uses weak XOR logic

No strong cryptographic algorithm like AES
