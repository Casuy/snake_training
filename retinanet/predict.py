from retinanet import Retinanet
from PIL import Image

retinanet = Retinanet()
image = Image.open("./img/street.jpg")
r_image = retinanet.detect_image(image)
r_image.show()
# while True:
#     img = input('Input image filename:')
#     try:
#         image = Image.open(img)
#     except:
#         print('Open Error! Try again!')
#         continue
#     else:
#         r_image = retinanet.detect_image(image)
#         r_image.show()
    