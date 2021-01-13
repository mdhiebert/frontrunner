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
from frontrunner.geo.terrain_reader import TerrainReader

sm = StaticMap(GOOGLE_API_KEY)
tr = TerrainReader()

im = sm.get_map('34.8940847,70.9105576', '13', '640x640', maptype='satellite', scale=2)
# im = sm.get_map('34.8940847,70.9105576', '13', '640x640', maptype='terrain', scale=2)

with open('photo.png', 'wb') as f:
    f.write(im)

im = cv2.imread('photo.png')
im = tr.get_sim_terrain(im)

mask = np.all(im != (0,0,0), axis=-1)

green = np.zeros(im.shape, dtype=np.uint8)
green[mask] = (255, 0, 0)


im = cv2.imread('photo.png')

overlay = cv2.addWeighted(im,1,green,0.5,0)
cv2.imwrite('altphoto.png', overlay)


# kernel = np.array([[-1,-1,-1], 
#                        [-1, 9,-1],
#                        [-1,-1,-1]])

# im = cv2.filter2D(im, -1, 2 * kernel)
# # im = cv2.medianBlur(im,3)
# # im = cv2.filter2D(im, -1, kernel)
# ret, threshold = cv2.threshold(im,0,255,cv2.THRESH_BINARY)
# contours, _= cv2.findContours(threshold, cv2.RETR_TREE, 
#                                cv2.CHAIN_APPROX_SIMPLE) 
# im[im > 154] = 255

# threshold = cv2.adaptiveThreshold(im,220,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,27,10)

# cv2.imshow('o', im)
# cv2.waitKey(0)
