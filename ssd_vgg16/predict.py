from ssd import SSD
from PIL import Image

ssd = SSD()
image = Image.open("./img/street.jpg")
r_image = ssd.detect_image(image)
r_image.show()

# while True:
#     img = input('Input image filename:')
#     try:
#         image = Image.open(img)
#     except:
#         print('Open Error! Try again!')
#         continue
#     else:
#         r_image = ssd.detect_image(image)
#         r_image.show()
# #ssd.close_session()
    