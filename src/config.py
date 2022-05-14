import os

# Path Definitions
BASE_PATH = os.getcwd()
GIF_LAYERS_PATH = os.path.join(BASE_PATH,'gif_layers')
GIF_DECONSTRUCTED_LAYERS_PATH = os.path.join(BASE_PATH,'gif_deconstructed_layers')
BUILD_PATH = os.path.join(BASE_PATH, 'build')
SAVE_IMAGE_PATH = os.path.join(BUILD_PATH, 'images')
SAVE_METADATA_PATH = os.path.join(BUILD_PATH, 'json')

# How many GIFs will be randomly generated
GENERATION_COUNT = 1

LAYERS_ORDER = [
    'background',
    'body',
    'ears',
    'head',
    'eyes',
    'hair',
    'mouth'
]

# Metadata Constants
METADATA_NAME = 'Your NFT Collection'                           # Name of NFT collection
METADATA_DESCRIPTION = "A collection of 10,000 GIF NFTs"        # Description of collection

# Toggle between saving as a .GIF or .MP4
SAVE_AS_MP4 = True
