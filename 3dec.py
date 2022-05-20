#pip install wheel steganocryptopy
from steganocryptopy.steganography import Steganography
# Decrypt the data from image
decrypted_text = Steganography.decrypt(key, output_image)

print(decrypted_text)

Steganography.write_file(output_file, decrypted_text)