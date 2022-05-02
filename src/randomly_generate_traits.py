import random
from config import * 

generated_trait_list = []

# Iterates over the layers in LAYERS_ORDER & appends both the trait type/value to an object, & corresponding trait value path to an array 
def generate_traits():
    trait_obj = {}
    trait_paths = []

    for trait in LAYERS_ORDER:
        trait_path = os.path.join(BUILD_PATH, GIF_DECONSTRUCTED_LAYERS_PATH, trait)
        trait_selection = select_trait(trait_path)
        trait_obj.update({trait: os.path.split(trait_selection)[1]})
        trait_paths.append(trait_selection)

    # Check that this trait sequence isn't already present in the overall trait list before returning
    trait_str = generate_string_of_traits(trait_obj)
    if trait_str in generated_trait_list:
        print(f'Trait list has already been generated - trying another sequence of random traits')
        generate_traits()
    generated_trait_list.append(trait_str)
    return [trait_obj, trait_paths]


# Returns the full path to a randomly selected trait value option, given the layer path to that trait type 
def select_trait(trait_path):
    # Only looking at subdirectories, as they should be parsed PNGs of the GIFs
    trait_options = [ f.path for f in os.scandir(trait_path) if f.is_dir() ]
    random_trait = random.choice(trait_options)
    return random_trait


# Turns object into a string that gets added to generated_trait_list for ensuring trait selection is unique 
def generate_string_of_traits(trait_obj):
    trait_str = ''
    for key in trait_obj.keys():
        trait_str+=(key + trait_obj[key])
    return trait_str