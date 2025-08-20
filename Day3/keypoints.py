import cv2
import matplotlib.pyplot as plt
img=cv2.imread("building.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray,None)
img_sift = cv2.drawKeypoints(img,keypoints,None,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(cv2.cvtColor(img_sift,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()