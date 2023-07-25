import colorgram

# Extract colors from an image
colors = colorgram.extract("image.jpg", 100)

extracted_colors = []

for rgb_color in colors:
    r = rgb_color.rgb[0]
    g = rgb_color.rgb[1]
    b = rgb_color.rgb[2]
    extracted_color = (r, g, b)
    extracted_colors.append(extracted_color)

print(extracted_colors)