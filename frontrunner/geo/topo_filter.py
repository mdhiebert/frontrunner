
from PIL import Image
import numpy as np
import cv2
from frontrunner.geo.google.maps import StaticMap
from frontrunner.utils import utils

def main(key):
    sm = StaticMap(key)

    # im = sm.get_map('34.8940847,70.9105576', '13', '640x640', maptype='satellite', scale=2)
    im = sm.get_map('34.8940847,70.9105576', '13', '640x640', maptype='terrain', scale=2)
    with open('photo.png', 'wb') as f:
        f.write(im)


    im = cv2.imread('photo.png', cv2.IMREAD_GRAYSCALE) 
    real_image = cv2.imread('photo.png')
    contour_kernel = np.array([[-1,-1,-1], 
                        [-1, 9,-1],
                        [-1,-1,-1]])

    im = cv2.filter2D(im, -1, 2 * contour_kernel)
    # im = cv2.medianBlur(im,3)
    # im = cv2.filter2D(im, -1, kernel)
    ret, threshold = cv2.threshold(im,0,255,cv2.THRESH_BINARY)
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE, 
                                cv2.CHAIN_APPROX_SIMPLE) 
    # im[im > 154] = 255

    # threshold = cv2.adaptiveThreshold(im,220,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,27,10)

    cv2.imwrite('1filter_photo.png', im)
    _, closedPixels = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite('closed_pixels.png', closedPixels)

    kern = utils.get_kern(25)
    #print(type(kern))
    adjacentToClosedPixels = cv2.filter2D(closedPixels, -1, kern)
    cv2.imwrite('close_to_closed_pixels.png', adjacentToClosedPixels)
    im[np.where(adjacentToClosedPixels == 255)] = [0]
    cv2.imwrite('eligible.png', im)

    real_image[np.where(im == 255)] = [128,0,128]
    cv2.imwrite('eligible_marked.png', real_image)
    open_pixels = []
    for i in range(len(im)):
        for j in range(len(im[0])):
            
            if im[i, j] != 0:
                print(i, j)
                open_pixels.append((j, i))
    # open_pixels = np.argwhere(real_image == 255)
    # print(open_pixels)
    #print("open from topo", open_pixels)
    return open_pixels