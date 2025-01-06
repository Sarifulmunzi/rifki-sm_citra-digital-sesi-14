import numpy as np
import imageio
import matplotlib.pyplot as plt

def encrypt_image(image, key):
    key = np.resize(key, image.shape)
    encrypted_image = np.bitwise_xor(image, key)
    return encrypted_image

def decrypt_image(encrypted_image, key):
    key = np.resize(key, encrypted_image.shape)
    decrypted_image = np.bitwise_xor(encrypted_image, key)
    return decrypted_image

image_path = 'Screenshot (2).jpg'
image = imageio.imread(image_path)

plt.imshow(image)
plt.title('Citra Asli')
plt.axis('off')
plt.show()

key = np.random.randint(0, 256, size=image.shape, dtype=np.uint8)

encrypted_image = encrypt_image(image, key)

plt.imshow(encrypted_image)
plt.title('Citra Terenkripsi')
plt.axis('off')
plt.show()

decrypted_image = decrypt_image(encrypted_image, key)

plt.imshow(decrypted_image)
plt.title('Citra Terdekripsi')
plt.axis('off')
plt.show()

imageio.imwrite('encrypted_image.png', encrypted_image)
imageio.imwrite('decrypted_image.png', decrypted_image)