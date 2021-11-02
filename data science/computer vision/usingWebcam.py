import cv2

# img = cv2.imread('../coin.jpg')

# cv2.imshow( 'using opencv', img )

# cv2.waitKey(5000)

# cap = cv2.VideoCapture(0)

# using a videofile as source
cap = cv2.VideoCapture("fetch_video.webm")


while True:

    ret, frame = cap.read()

    print(ret)

    cv2.imshow('using webcam', frame)

    if cv2.waitKey(100) & 0xFF == ord('a'):
        break

cv2.destroyAllWindows()
cap.release()
