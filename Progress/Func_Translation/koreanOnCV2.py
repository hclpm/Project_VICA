import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

frame = np.full((500, 500, 3), 255, np.uint8)
text = "한글 출력"
font = ImageFont.truetype('C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/Main/NanumBarunGothicLight.ttf', 15)

img_pil = Image.fromarray(frame)
draw = ImageDraw.Draw(img_pil)

# 텍스트가 들어갈 사각형의 크기 계산
text_size = draw.textsize(text, font)
rect_size = (text_size[0] + 10, text_size[1] + 10)  # 여백을 추가하여 텍스트 주위에 여백을 둡니다.

# 검은색 사각형 그리기
draw.rectangle([(0, 30), (50 + rect_size[0], 300 + rect_size[1])], fill=(0, 0, 0))

# 텍스트 추가
draw.text((50 + 5, 300 + 5), text, (255, 255, 255), font=font)  # 여백 만큼 이동해서 텍스트를 그립니다.

frame = np.array(img_pil)

cv2.imshow("window", frame)
cv2.waitKey()
cv2.destroyAllWindows()