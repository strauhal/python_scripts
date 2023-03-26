from PIL import Image

# Open the image
image = Image.open('input_image.jpg')

# Create a new image with the new width
new_width = image.width + 1024
new_image = Image.new('RGB', (new_width, image.height), (255, 255, 255))

# Paste the original image onto the new image with a 1024 pixel offset
new_image.paste(image, (1024, 0))

# Save the new image
new_image.save('output_image.jpg')
