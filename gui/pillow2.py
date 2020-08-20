from PIL import Image, ImageTk

im = Image.open("./resource/dog.jpg")

# Thumbnail 이미지 생성
size = (64, 64)
im.thumbnail(size)

im.save("./resource/python-thumb.jpg")

