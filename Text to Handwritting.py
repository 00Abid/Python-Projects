import pywhatkit as kit
import cv2
kit.text_to_handwriting("Abid is best " , save_to = "handwritting.png")
img = cv2.imread("handwritting.png")
cv2.imshow("Text to Handwritting" , img)
cv2.waitKey()
cv2.destroyAllWindows()