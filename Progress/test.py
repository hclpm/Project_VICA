def camera():
    import cv2
    print('cam activated')
    # open cam
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('VideoCall', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break
    cap.release()
    cv2.destroyAllWindows()
    print("cam_thread closed")

camera()