from pathlib import Path
import cv2
import numpy as np
from os.path import basename, join, splitext
import time
from frontrunner.path_generation.new_a_star import pyastar

config = {}
exec(Path('config.py').read_text(), config)
DEPLOYMENT_VARS = config['DEPLOYMENT_VARS']

# input/output files
MAZE_FPATH = DEPLOYMENT_VARS.path + '/contours_reconstructed.png'
OUTP_FPATH = DEPLOYMENT_VARS.path + '/intel_solved.png'

def compute_path(start, end):
    maze = cv2.imread(MAZE_FPATH)
    if maze is None:
        print('no file found: %s' % (MAZE_FPATH))
        return
    grid = cv2.cvtColor(maze, cv2.COLOR_BGR2GRAY).astype(np.float32)
    grid[grid == 255] = 1
    grid[grid == 0] = np.inf

    assert grid.min() == 1, 'cost of moving must be at least 1'

    # set allow_diagonal=True to enable 8-connectivity
    path = pyastar.astar_path(grid, start, end, allow_diagonal=DEPLOYMENT_VARS.search_diagonally)
    
 

    if path.shape[0] > 0:
        #print('Found path of length %d' % (path.shape[0]))
        maze[path[:, 0], path[:, 1]] = (0, 0, 255)

        cv2.imwrite(OUTP_FPATH, maze)
    else:
        #print('no path found')
        pass

    return path

def main(start, end):
    '''
    This library holds the convention that pixels are represented as (x, y) 
    with (0, 0) being the upper left hand corner.
    '''
    
    start = np.array([start[0], start[1]])
    end = np.array([end[0], end[1]])
    # print("START:", start)
    # print("end", end)
    path = compute_path(start, end)
    path = [tuple(x) for x in path]
    
    return path

