import cv2
import os

# 저장할 이미지 폴더 지정
output_folder = 'C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/CollectDataViaCam/FaceData/Kwang'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 카메라 열기
cap = cv2.VideoCapture(0)  # 0은 기본 카메라

# 이미지 번호 초기화
img_count = 0

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 화면에 프레임 표시
    cv2.imshow('Camera', frame)

    # 스페이스바를 눌렀을 때 이미지 캡쳐
    key = cv2.waitKey(1)
    if key == 32:  # 32는 스페이스바의 ASCII 코드
        img_count += 1
        img_name = os.path.join(output_folder, f"captured_image_{img_count}.png")
        cv2.imwrite(img_name, frame)
        print(f"Captured image saved as {img_name}")

    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        break

# 사용한 자원 해제
cap.release()
cv2.destroyAllWindows()