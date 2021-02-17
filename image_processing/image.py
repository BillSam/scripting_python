from PIL import Image, ImageFilter

img = Image.open('./poked/4.3 pikachu.jpg')
print(img.format)
print(img.size)
print(img.mode)

# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
filtered_img = filtered_img.save("blur.png", 'png')
