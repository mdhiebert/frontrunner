import cv2 as cv
import numpy as np
from scipy.spatial import distance as dis
from skimage.draw import line
# being start and end two points (x1,y1), (x2,y2)

def find_optimal_straightline(im, dest_x, dest_y, open_pixels):
    best = np.Inf
    sp = (dest_x, dest_y)
    destination = (dest_x, dest_y)
    print("num open_pixels", len(open_pixels))
    for pixel in open_pixels:
        #print("pixel", pixel)
        distance = dis.euclidean((dest_x, dest_y), pixel)
        #print(distance)
        if distance < best:
            best = distance
            sp = (pixel[0], pixel[1])
    print(destination)
    print(sp)
    pts = cv.line(im, destination, sp, (128,0,128), 1)
    pts = list(zip(*line(*sp, *destination)))
    cv.circle(im,sp,4,(34,139,34),-1)
    cv.circle(im,destination,4,(0,0,255),-1)

    print(pts)

def find_optimal_elevation(im, dest_x, dest_y, open_pixels):
    return None

def find_optimal_avoid_lda(im, dest_x, dest_y, open_pixels):
    return None

def find_and_draw_routes(im, dest_x, dest_y, open_pixels):
    optimal_straightline = find_optimal_straightline(im, dest_x, dest_y, open_pixels)
    optimal_elevation = find_optimal_elevation(im, dest_x, dest_y, open_pixels)
    optimal_avoid_lda = find_optimal_avoid_lda(im, dest_x, dest_y, open_pixels)
    
    return [optimal_straightline, optimal_elevation, optimal_avoid_lda]
    