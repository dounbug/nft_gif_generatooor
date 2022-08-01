import os

# Path Definitions
BASE_PATH = os.getcwd()
GIF_LAYERS_PATH = os.path.join(BASE_PATH,'gif_layers')
GIF_DECONSTRUCTED_LAYERS_PATH = os.path.join(BASE_PATH,'gif_deconstructed_layers')
BUILD_PATH = os.path.join(BASE_PATH, 'build')
SAVE_IMAGE_PATH = os.path.join(BUILD_PATH, 'images')
SAVE_METADATA_PATH = os.path.join(BUILD_PATH, 'json')
SAVE_THUMBNAIL_PATH = os.path.join(BUILD_PATH, 'thumbnail')

# Order in which to generate individual PNGs 
LAYERS_ORDER = [
    'background',
    'body',
    'ears',
    'head',
    'eyes',
    'hair',
    'mouth',
    'accessories'
]

INCOMPATIBLE_TRAITS = {
    'background': [],
    'body' : []
}

# Generation constants
NUMBER_OF_FRAMES = 120
FRAME_RATE = 24
SAVE_THUMBNAIL = True
GENERATION_COUNT = 3

# Metadata Constants
METADATA_NAME = 'Your NFT Collection'                           # Name of NFT collection
METADATA_DESCRIPTION = "A collection of 10,000 GIF NFTs"        # Description of collection