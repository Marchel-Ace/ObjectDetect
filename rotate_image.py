import os 
import cv2


image_dir = os.path.join("datasets", "images/test")

for root, dirs, files in os.walk(image_dir):
    for file in files:
        image = cv2.imread(os.path.join(root, file))
        cv2.imwrite(os.path.join(root, file), image)