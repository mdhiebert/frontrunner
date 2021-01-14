import cv2 as cv
import numpy as np
from scipy.spatial import distance as dis
from skimage.draw import line
from frontrunner.path_generation.new_a_star.search import compute_path
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

    print("_________")
    pts = cv.line(im, destination, sp, (128,0,128), 1)
    pts = list(zip(*line(*sp, *destination)))
    cv.circle(im,sp,4,(34,139,34),-1)
    cv.circle(im,destination,4,(0,0,255),-1)

def find_optimal_elevation(im, drawable_im, dest_x, dest_y, open_pixels):
    imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 175, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    img = cv.drawContours(imgray, contours, -1, (0,255,75), 1)
    ret, thresh = cv.threshold(img, 254, 255, 0)
    cv.imwrite("contours_reconstructed.png", thresh)

    best = np.Inf
    sp = (dest_x, dest_y)
    destination = (dest_x, dest_y)
    best_path = None
    for pixel in open_pixels:
        path = compute_path(pixel, destination)
        if len(path) > 0 and len(path) < best:
            best = len(path)
            best_path = path
            sp = pixel
    print(sp)
    print(destination)
    cv.circle(drawable_im,sp,4,(128,0,0),-1)
    for pt in best_path:
        drawable_im[pt[1], pt[0]] = [128,0,40]

def find_optimal_avoid_lda(im, dest_x, dest_y, open_pixels):
    return None

def find_and_draw_routes(topo_im, open_pixel_im, dest_x, dest_y, open_pixels):
    optimal_straightline = find_optimal_straightline(open_pixel_im, dest_x, dest_y, open_pixels)
    optimal_elevation = find_optimal_elevation(topo_im, open_pixel_im, dest_x, dest_y, open_pixels)
    optimal_avoid_lda = find_optimal_avoid_lda(topo_im, dest_x, dest_y, open_pixels)
    
    return [optimal_straightline, optimal_elevation, optimal_avoid_lda]
    