import cv2
import numpy as np

from scipy import stats
from collections import defaultdict
import operator

class TerrainReader:
    def __init__(self) -> None:
        super().__init__()

    def reduce_colors(self, image, div=64):

        quantized = image // div * div + div // 2

        return quantized

    def get_sim_terrain(self, image):
        '''
            Returns a binary image with regions acceptable for landing based solely on satellite imagery as 1, 0 else.
        '''
        
        reduced_image = self.reduce_colors(image, 128)
        mode_pix = self._get_mode_pixel(reduced_image)

        # mask away the mode pixel
        mask = np.all(reduced_image == mode_pix, axis=-1)

        sim_image = 255 * np.ones(reduced_image.shape)
        sim_image[mask] = np.zeros((3,))

        return sim_image

    def _get_mode_pixel(self, image):
        count = defaultdict(lambda: 0)

        for row in image:
            for col in row:
                pix = tuple(col)
                count[pix] += 1

        return max(count.items(), key=operator.itemgetter(1))[0]

        



