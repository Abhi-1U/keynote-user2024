from PIL import Image

# Define the size of the image
width = int(1920 * 0.3)
height = 1080

# Create a plain yellow image

slate_image = Image.new("RGB", (width, height), "darkviolet")
slate_image.save("/home/abhi/Documents/UseR-24-slides/resources/darkviolet_image.png")

# Display image size to confirm
slate_image.size