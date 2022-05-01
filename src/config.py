from pathlib import Path
import os
from PIL import Image

#Path Definition
BASE_PATH = os.getcwd()
GIF_LAYERS_PATH = os.path.join(BASE_PATH,'gif_layers')
GIF_DECONSTRUCTED_LAYERS_PATH = os.path.join(BASE_PATH,'gif_deconstructed_layers')

LAYERS_ORDER = {
    'background',
    'body'
}
