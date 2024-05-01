import cv2
import time
import os

# Create the directory if it doesn't exist
if not os.path.exists("real_image"):
    os.makedirs("real_image")

cam = cv2.VideoCapture(0)

cv2.namedWindow("real time image of parking lot")
img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break
    
    cv2.imshow("real time image of parking lot", frame)

    # Check for key press
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing app")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("screenshot taken")
        img_counter += 1
    
    # Take a screenshot every 5 seconds
    time.sleep(5)
    img_name = os.path.join("real_image", "real_image_{}.png".format(img_counter))
    cv2.imwrite(img_name, frame)
    print("Screenshot taken")
    img_counter += 1

cam.release()
cv2.destroyAllWindows()
