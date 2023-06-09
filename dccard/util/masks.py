from PIL import Image
import os

path = os.path.dirname(os.path.abspath(__file__))
def circle_mask(size):
    mask = Image.open(path + '/assets/circle.ppm')
    mask = mask.convert('L')
    mask = mask.resize((size, size))
    return mask


