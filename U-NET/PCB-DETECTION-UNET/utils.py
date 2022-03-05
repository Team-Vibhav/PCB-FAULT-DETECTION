import cv2

from tqdm.notebook import tqdm
from PIL import Image
import os



def load_data(path):
    mask_path = "mask"
    input_path = "images"
    image_path = os.path.join(path,input_path)
    mask_path = os.path.join(path,mask_path)
    pcb_images = []
    for img_path in tqdm(sorted(os.listdir(image_path)),total=len(os.listdir(image_path))):
        img = cv2.imread(os.path.join(image_path,img_path))
        img = cv2.resize(img,(256,256))
        pcb_images.append(img)

    pcb_mask = []
    for msk_path in tqdm(sorted(os.listdir(mask_path)),total=len(os.listdir(mask_path))):
        mask = cv2.imread(os.path.join(mask_path,msk_path), cv2.IMREAD_GRAYSCALE)
        mask = cv2.resize(mask,(256,256))
        pcb_mask.append(mask)
    return pcb_images,pcb_mask

def load_data(path):
    mask_path = "mask"
    input_path = "images"
    image_path = os.path.join(path,input_path)
    mask_path = os.path.join(path,mask_path)
    pcb_images= []
    for img_path in os.listdir(image_path):
        img = cv2.imread(os.path.join(image_path,img_path))
        img = cv2.resize(img,(256,256))
        pcb_images.append(img)


    pcb_mask =[]
    for msk_path in os.listdir(mask_path):
        mask = cv2.imread(os.path.join(mask_path,msk_path), cv2.IMREAD_GRAYSCALE)
        mask = cv2.resize(mask,(256,256))
        pcb_mask.append(mask)
    return image_path,pcb_images

if __name__ == "__main__":
    path = os.getcwd()
    path = os.path.join(path,"final-set")
    image_path,pcb_images = load_data(path)
    print(image_path,pcb_images)