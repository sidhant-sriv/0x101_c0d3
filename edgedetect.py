#This is edge detect filter in Pillow
from PIL import Image, ImageFilter

image = Image.open(r"/home/sidhant/Pictures/Webcam/sidface.jpg")

image = image.convert("L")
# image = image.filter(ImageFilter.FIND_EDGES)
# image.save(r"sidface_edgy.png")
final = image.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,-1, -1, -1, -1), 1, 0))
final.save(r"sidface_laplaceedgy2.png")
