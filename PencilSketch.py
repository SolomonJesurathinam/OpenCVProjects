import cv2

def resize_func(image):
    original_shape = image.shape
    if original_shape[0] >= 1000:
        scale_percent = 30  # percent of original size
    else:
        scale_percent = 90  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return img
def PencilnBlack(img,blurValue):
    #img = cv2.imread("alan-walker.jpg")
    img = resize_func(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    neg = 255-gray
    blur = cv2.GaussianBlur(neg,ksize=(blurValue,blurValue),sigmaX=0,sigmaY=0) #21
    pencil = cv2.divide(gray,255-blur,scale=256)
    return pencil
'''
cv2.imshow("Original img",img)
cv2.imshow("pencil",pencil)
cv2.imshow("pencil1",black)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
