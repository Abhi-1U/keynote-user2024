from PIL import Image, ImageDraw

# Create a new image with white background
image_width, image_height = 576, 1080

map_image = Image.new("RGB", (image_width, image_height), "white")
draw = ImageDraw.Draw(map_image)

# Draw simplified representations of the countries
# Approximate coordinates for the highlighted countries (relative positions)
countries_coords = {
    "United Kingdom": (150, 300),
    "France": (170, 350),
    "India": (300, 600),
    "China": (350, 550),
    "Australia": (450, 850),
    "United States of America": (80, 400)
}

# Draw circles to represent the countries
for country, (x, y) in countries_coords.items():
    draw.ellipse((x-20, y-20, x+20, y+20), fill="red")

# Save the image
map_image.save("simplified_world_map.png")

map_image.size

