from generate_gif import *

filepaths = find_filepaths({
    'background': 'black_forest', 
    'body': 'black_cape', 
    'ears': 'green_slime', 
    'head': 'HEAD_10', 
    'eyes': 'EYES_16', 
    'hair': 'weirdo', 
    'mouth': 'MOUTH_7'
})

generate_single_image(filepaths)