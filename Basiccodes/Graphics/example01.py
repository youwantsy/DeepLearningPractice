import cv2

filepath = "C:/JSY/images/bichon01.jpg"
img = cv2.imread(filepath)

img = cv2.line(img, (20, 60), (350, 60), (255,0,255), 2, cv2.LINE_AA)
img = cv2.circle(img, (80, 120), 10, (255,255,0), 2, cv2.LINE_AA)
img = cv2.rectangle(img, (80,120), (380,430), (255,255,0),2)

img = cv2.putText(img, "BICHON", (30, 50),
                  cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                  1.5, (0, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("main", img)
cv2.waitKey()
cv2.destroyWindow("main")