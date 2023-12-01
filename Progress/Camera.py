import cv2

# open cam
cap = cv2.VideoCapture(0)

subtitle = "Hello"  # initial subtitle

while True:
    ret, frame = cap.read()
    # Inversion
    frame = cv2.flip(frame, 1)
    #print subtitle
    cv2.putText(frame, subtitle, (10, frame.shape[0] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow('Face Detection', frame)
    
    # 키보드 입력 받기
    key = cv2.waitKey(1) & 0xFF

    # 'q'를 누르면 종료
    if key == ord('q'):
        break
    # 't'를 누르면 자막 변경
    elif key == ord('t'):
        subtitle = "t"

# close cam
cap.release()
cv2.destroyAllWindows()