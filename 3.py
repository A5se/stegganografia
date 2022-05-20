#pip install wheel steganocryptopy
from steganocryptopy.steganography import Steganography


key = 'key.key'             # Key file name
input_image = 'img/3.png'   # Image name
input_file = 'secret_message.txt'      # File that needs to be encrypted
output_image = '3_secret.png' # Output image name
output_file = 'secret.txt'  # Output file name

# Generate key
Steganography.generate_key(key)

# Encrypt the data and store in the image
encrypted_image = Steganography.encrypt(key, input_image, input_file)
encrypted_image.save(output_image)
