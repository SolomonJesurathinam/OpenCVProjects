import cv2
import os
import matplotlib.pyplot as plt

def Image(img,frame_name):
    output_folder = 'output'
    cv2.imshow(frame_name,img)
    cv2.imwrite(os.path.join(output_folder,frame_name+'.jpg'),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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

def output(img,blur,edge,bFilter):
    img=resize_func(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,blur) #3
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,edge,edge) #5
    col_img = cv2.bilateralFilter(img,bFilter,255,255) #5
    cartoon = cv2.bitwise_and(col_img,col_img,mask=edges)
    image = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    return image

#plt.imshow(image)
#plt.show()

