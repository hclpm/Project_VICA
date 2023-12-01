import threading
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image 

font = ImageFont.truetype('C:/Users/js2-3/Desktop/Github/Desktop_sync/Projects/Communication_Assistant/VideoCall/NanumGothic.ttf', 20)
img = np.full((480,640,3), 0, np.int8)
cv2.rectangle(img, (0, 0), (480, 600), (0, 0, 0), -1)
text = "한글 출력"
img_pil = Image.fromarray(img.astype(np.uint8))
draw = ImageDraw.Draw(img_pil)
draw.text((50,300), text, (0,0,255), font=font)
img = np.array(img_pil)
cv2.rectangle(img, (0, 0), (480, 600), (0, 0, 0), -1)
print("Img shape:", img.shape)


cv2.imshow("korean", img)
cv2.waitKey()
cv2.destroyAllWindows()