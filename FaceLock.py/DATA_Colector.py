import cv2 as cv
import time
import os 
from Objects import user1


global img_number
img_number = 1
img_range = range(1, 20)
t = 0.5
class_name = user1.first


def dataset():
    os.makedirs(f"Img_Dataset_{class_name}", exist_ok=True)

    cv.imwrite(f"Img_Dataset_{class_name}/{img_number}.jpg", user_feed)


cap = cv.VideoCapture(0)

while True:
    ret, user_feed = cap.read()

    cv.imshow("User_image_feed", user_feed)

    key = cv.waitKey(1) & 0xFF

    if key == ord("m"):
        
        for i in img_range:
            ret, user_feed = cap.read()
            cap = cv.VideoCapture(0)
            dataset()
            img_number += 1
            time.sleep(t)
        
        cap.release()
            

    elif key == ord("q"):
        break

cap.release()
cv.destroyAllWindows()

