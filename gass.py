import cv2
def edgedetectusingcannyandgaussian(img):
# cv2.imshow('Original', img)
  cv2.waitKey(0)
  img_blur = cv2.GaussianBlur(img, (3,3), 0)
  sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis

  sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
  sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

  edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
  return edges