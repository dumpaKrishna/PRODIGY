from PIL import Image

def encrypt_image(image_path, key):

    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Simple pixel swapping based on the key
            new_x = (x + key) % width
            new_y = (y + key) % height

            pixels[x, y] = pixels[new_x, new_y]
            pixels[new_x, new_y] = (r, g, b)

    return img

def decrypt_image(encrypted_image, key):

    return encrypt_image(encrypted_image, -key)

image_path = "Only.png"
key = 10

encrypted_image = encrypt_image(image_path, key)
encrypted_image.save("encrypted_image.png")

decrypted_image = decrypt_image("encrypted_image.png", key)
decrypted_image.save("decrypted_image.png")