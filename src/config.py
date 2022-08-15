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
    # BODY 
    'Hells_Cook': ['Aurora', '5th_Dimension', 'Blood_Lust'],
    # EARS
    'Blue_Flame_Ears': ['Rainbow_Rock_Tee', 'Extraterrestrial', 'Suspicious'],
    # HEAD
    'Acid_Wash_Head': ['Aftermath', 'Casual_Muck', 'Handmade_Bomber', 'OctoTutu', 'Purple_Fire_Coat'],
    'Ash_Cloud': ['Aftermath', 'Casual_Muck', 'Handmade_Bomber', 'OctoTutu', 'Purple_Fire_Coat'],
    'Atomic_Alien': ['Aftermath', 'Casual_Muck', 'Handmade_Bomber', 'OctoTutu', 'Purple_Fire_Coat'],
    'Bleeding_Chrome_Head': ['Aftermath', 'Casual_Muck', 'Handmade_Bomber', 'OctoTutu', 'Purple_Fire_Coat'],
    'Bleeding_Gold_Head': ['Aftermath', 'Casual_Muck', 'Handmade_Bomber', 'OctoTutu', 'Purple_Fire_Coat'],
    'Bleeding_Metal_Head': ['Aftermath', 'Casual_Muck', 'Handmade_Bomber', 'OctoTutu', 'Purple_Fire_Coat'],
    'Extraterrestrial': ['Aftermath', 'Casual_Muck', 'Handmade_Bomber', 'OctoTutu', 'Purple_Fire_Coat'],

    # HAIR
    'Amoeba_Hair': ['Aurora', '5th_Dimension', 'Blood_Lust', 'Barbie_Inferno', 'Abandoned_Power_Plant', 'Aftermath'],
    'Atomic_Hair': ['Aurora', '5th_Dimension', 'Blood_Lust', 'Barbie_Inferno', 'Abandoned_Power_Plant', 'Aftermath'],
    'BoneyTail': ['Aurora', '5th_Dimension', 'Blood_Lust', 'Barbie_Inferno', 'Abandoned_Power_Plant', 'Aftermath'],
    'Dead_Foliage': ['Aurora', '5th_Dimension', 'Blood_Lust', 'Barbie_Inferno', 'Abandoned_Power_Plant', 'Aftermath'],
    'Electric_Wig': ['Aurora', '5th_Dimension', 'Blood_Lust', 'Barbie_Inferno', 'Abandoned_Power_Plant', 'Aftermath'],
    'Erupting_Bun': ['Aurora', '5th_Dimension', 'Blood_Lust', 'Barbie_Inferno', 'Abandoned_Power_Plant', 'Aftermath'],
    'Evil_Bob': [],

    #ACCESSORIES
    # 'Calcium_Chain': ['Bored_AF', 'Burst_Vessels_Eyes', 'Bursting_Eye', 'Snake_Eyes', 'Suspicious', 'Void_Eyes']
}

# Generation constants
NUMBER_OF_FRAMES = 120
FRAME_RATE = 24
SAVE_THUMBNAIL = True
GENERATION_COUNT = 1

# Metadata Constants
METADATA_NAME = 'Your NFT Collection'                           # Name of NFT collection
METADATA_DESCRIPTION = "A collection of 10,000 GIF NFTs"        # Description of collection