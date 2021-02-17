from PIL import Image, ImageFilter

img = Image.open('./poked/4.3 pikachu.jpg')
print(img.format)
print(img.size)
print(img.mode)

# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert('L')
# filtered_img = filtered_img.save("blur.png", 'png')
# filtered_img.show()
# crooked = filtered_img.rotate(90)
# crooked.save("grey.png", 'png')
# crooked = filtered_img.resize((300, 300))
# crooked.save("resize.png", 'png')
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("cropped.png", 'png')
# img.thumbnail(400,400)


