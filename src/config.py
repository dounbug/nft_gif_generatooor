import os

# Path Definitions
BASE_PATH = os.getcwd()
GIF_LAYERS_PATH = os.path.join(BASE_PATH,'gif_layers')
GIF_DECONSTRUCTED_LAYERS_PATH = os.path.join(BASE_PATH,'gif_deconstructed_layers')
BUILD_PATH = os.path.join(BASE_PATH, 'build')
SAVE_IMAGE_PATH = os.path.join(BUILD_PATH, 'images')
SAVE_METADATA_PATH = os.path.join(BUILD_PATH, 'json')
SAVE_THUMBNAIL_PATH = os.path.join(BUILD_PATH, 'thumbnail')

#Convert Gif to Py Script Constants
NUMBER_OF_FRAMES = 120
FRAME_RATE = 24

# How many GIFs will be randomly generated
GENERATION_COUNT = 3

# Duration of final output (in seconds)
GIF_DURATION = 4

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

# Metadata Constants
METADATA_NAME = 'Your NFT Collection'                           # Name of NFT collection
METADATA_DESCRIPTION = "A collection of 10,000 GIF NFTs"        # Description of collection


# Toggle between saving as a .GIF or .MP4
SAVE_AS_MP4 = True
