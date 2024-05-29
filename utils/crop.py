import numpy as np
import cv2
import os

print("Starting batch crop")

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

images = load_images_from_folder('start')

for num, img in enumerate(images, start=0):
    height, width, channels = img.shape
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Crop out discription
    for dis in range(height):
        if(img_grey[dis,0] == 255):
            break

    img_cropped_dis = img[0:dis, :]
    height_dis, width_dis, channels = img_cropped_dis.shape
    img_cropped_dis_grey = cv2.cvtColor(img_cropped_dis, cv2.COLOR_BGR2GRAY)

    # Crop out black boarder X & Y
    for x in range(width_dis):
        if(img_cropped_dis_grey[height_dis//2, x] != 0):
            break

    for y in range(height_dis):
        if (img_cropped_dis_grey[y, width_dis//2] != 0):
            break

    img_cropped = img_cropped_dis[y:height_dis-y, x:width_dis-x]

    img = cv2.imwrite(os.path.join('end', 'output'+str(num)+'.jpg'), img_cropped)



