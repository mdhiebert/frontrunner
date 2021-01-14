# Python program to get a google map 
# image of specified location using 
# Google Static Maps API 

# importing required modules 
# import requests
# from creds import GOOGLE_API_KEY

# # url variable store url 
# url = "https://maps.googleapis.com/maps/api/staticmap?"

# # center defines the center of the map, 
# # equidistant from all edges of the map. 
# center = "Dehradun"

# # zoom defines the zoom 
# # level of the map 
# zoom = 10

# # get method of requests module 
# # return response object 
# r = requests.get('https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&style=feature:road|color:0x000000&maptype=terrain&key=') 

# # wb mode is stand for write binary mode 
# f = open('photo.jpg', 'wb') 

# # r.content gives content, 
# # in this case gives image 
# f.write(r.content) 

# # close method of file object 
# # save and close the file 
# f.close() 

from creds import GOOGLE_API_KEY
from PIL import Image
import numpy as np
import cv2
from frontrunner.geo.google.maps import StaticMap
import topo_test
from frontrunner.utils.route_search import find_and_draw_routes
import terrainmain

sm = StaticMap(GOOGLE_API_KEY)

# im = sm.get_map('34.8940847,70.9105576', '13', '640x640', maptype='satellite', scale=2)
im = sm.get_map('34.8940847,70.9105576', '13', '640x640', maptype='terrain', scale=2)
with open('photo.png', 'wb') as f:
    f.write(im)


im = cv2.imread('photo.png', cv2.IMREAD_GRAYSCALE) 
real_im = cv2.imread('photo.png')

kernel = np.array([[-1,-1,-1], 
                       [-1, 9,-1],
                       [-1,-1,-1]])

im = cv2.filter2D(im, -1, 2 * kernel)
# im = cv2.medianBlur(im,3)
# im = cv2.filter2D(im, -1, kernel)
ret, threshold = cv2.threshold(im,0,255,cv2.THRESH_BINARY)
contours, _= cv2.findContours(threshold, cv2.RETR_TREE, 
                               cv2.CHAIN_APPROX_SIMPLE) 
# im[im > 154] = 255

# threshold = cv2.adaptiveThreshold(im,220,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,27,10)

ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(im,(x,y),7,(0,0,0),-1)
        ix,iy = x,y

# Create a black image, a window and bind the function to window
cv2.namedWindow('map')
cv2.setMouseCallback('map',draw_circle)
cv2.moveWindow('map', 40,30)

topo_im = cv2.imread("filtered_photo.png")
while True:
    cv2.imshow('map',real_im)
    k = cv2.waitKey(20) & 0xFF
    if k == 15:
        break
    elif k == ord('a'):
        open_topo_pixels = set(topo_test.get_open_pixels())
        open_terrain_pixels = set(terrainmain.find_open_terrain())
        print("Finding intersection between 2 sets")
        open_pixels = list(open_topo_pixels.intersection(open_terrain_pixels))
        black_im = np.zeros((1280, 1280))
        for i in open_pixels:
            black_im[i] = 255
        cv2.imwrite("final_open_pixels.png", black_im)
        routes = find_and_draw_routes(topo_im, real_im, ix, iy, open_pixels)

cv2.destroyAllWindows()