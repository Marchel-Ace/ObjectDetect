import cv2
import os

for files in os.listdir('datasets/images/train/'):
    img = cv2.imread('datasets/images/train/' + files, cv2.IMREAD_UNCHANGED)
    
    print('Original Dimensions : ',img.shape)
    
    scale_percent = 60 # percent of original size
    width = int(720)
    height = int(960)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    print('Resized Dimensions : ',resized.shape)
    
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.imwrite('datasets/images/train/'+files, resized)  
   
cv2.destroyAllWindows()  
