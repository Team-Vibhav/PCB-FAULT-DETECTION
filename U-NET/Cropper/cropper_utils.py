import cv2
import os
import argparse
import numpy as np

def main(img_path,h = 500):
    img = cv2.imread(img_path)
    shape = img.shape
    w = int((shape[1]*500)/shape[0])
    img = cv2.resize(img,(w,h))
    
    edged,img_singlet = find_contors(img)
    while (True):
        cv2.imshow("image",img)
        cv2.imshow("canny",edged)
        cv2.imshow("Singlet",img_singlet)
        if cv2.waitKey(20) &0xFF ==27:
            break
        

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged

def find_contors(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_img, (3, 3), 0)
    edged = cv2.Canny(blurred, 30, 200)
    # edged = auto_canny(blurred)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contor = max_area_contour(contours)
    img_singlet = img.copy()
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    print(len(contours))
    cv2.drawContours(img_singlet, contor, -1, (0,255,0), 3)

    return edged,img_singlet

def max_area_contour(contours):
    max_area = 0
    for i in range(len(contours)):
        contour = contours[i]
        area = cv2.contourArea(contour)
        print(i,area)
        if area > max_area :
            max_area = area
            cont = contour
            print(i,area,"GG")
            
    return cont




if __name__ =="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image','--source', required=True, help="Image Path")
    args = vars(ap.parse_args())
    img = args['image']
    img_path = "imgs"
    path = os.path.join(img_path,img)

    main(path)
    
cv2.destroyAllWindows()