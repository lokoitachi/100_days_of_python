import colorgram


color_list = []

# Extracts 12 colors for the given image.

colors = colorgram.extract('image.jpg', 12)
print(colors)

for i in range(13):
    first_color = colors[i]
    color_list += first_color

print(color_list)