import random
from config import * 


# Iterates over the layers in LAYERS_ORDER & appends both the trait type/value to an object, & corresponding trait value path to an array 
def generate_trait_paths():
    trait_obj = {}
    trait_paths = []
    for trait in LAYERS_ORDER:
        trait_path = os.path.join(BUILD_PATH, GIF_DECONSTRUCTED_LAYERS_PATH, trait)
        trait_selection = select_trait(trait_path)
        trait_obj.update({trait: os.path.split(trait_selection)[1]})
        trait_paths.append(trait_selection)
    return [trait_obj, trait_paths]

        

# Returns the full path to a randomly selected trait value option, given the layer path to that trait type 
def select_trait(trait_path):
    # Only looking at subdirectories, as they should be parsed PNGs of the GIFs
    trait_options = [ f.path for f in os.scandir(trait_path) if f.is_dir() ]
    random_trait = random.choice(trait_options)
    return random_trait