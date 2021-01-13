import cv2 as cv

def find_optimal_straightline(im, dest_x, dest_y, open_pixels):
    
    pts = cv.line(im, (dest_x, dest_y), sp, (255, 0, 0), 3)

def find_optimal_elevation(im, dest_x, dest_y, open_pixels):
    return None

def find_optimal_avoid_lda(im, dest_x, dest_y, open_pixels):
    return None

def find_and_draw_routes(im, dest_x, dest_y, open_pixels):
    optimal_straightline = find_optimal_straightline(im, dest_x, dest_y, open_pixels)
    optimal_elevation = find_optimal_elevation(im, dest_x, dest_y, open_pixels)
    optimal_avoid_lda = find_optimal_avoid_lda(im, dest_x, dest_y, open_pixels)
    
    return [optimal_straightline, optimal_elevation, optimal_avoid_lda]
    