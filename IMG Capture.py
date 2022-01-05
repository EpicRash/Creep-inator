import cv2

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img,640,480)
    cv2.imshow("Video", img)
    cv2.waitKey(1)

