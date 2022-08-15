import random
from config import * 

generated_trait_list = []

# Iterates over the layers in LAYERS_ORDER & appends both the trait type/value to an object, & corresponding trait value path to an array 
def generate_traits():
    trait_obj = {}
    trait_paths = []

    for trait in LAYERS_ORDER:
        trait_path = os.path.join(BUILD_PATH, GIF_DECONSTRUCTED_LAYERS_PATH, trait)
        trait_selection = select_trait(trait_path, trait_obj)
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
def select_trait(trait_path, trait_obj):
    # Only looking at subdirectories, as they should be parsed PNGs of the GIFs
    trait_options = [ f.path for f in os.scandir(trait_path) if f.is_dir() ]
    rarity_weights = []
    for option in trait_options:
        option_arr = option.split('/')
        get_trait_weight(option_arr[len(option_arr)-1], rarity_weights)
  
    random_trait = random.choices(trait_options, weights=rarity_weights)[0]
    return check_incompatibility(random_trait, trait_path, trait_obj)


# Checks if currently selected trait is incompatible with any of the previously selected traits
def check_incompatibility(random_trait, trait_path, trait_obj):
    random_trait_value = os.path.split(random_trait)[1]
    if '#' in random_trait_value:
        random_trait_value = random_trait_value.split('#')[0]
    if random_trait_value in INCOMPATIBLE_TRAITS.keys():
        for value in trait_obj.values():
            if value in INCOMPATIBLE_TRAITS[random_trait_value]:
                print('Incompatibility found with traits {} and {}'.format(random_trait_value, value))
                return select_trait(trait_path, trait_obj)
    return random_trait


# Returns list of weighted traits, replacing traits that are missing a weight value with 1
def get_trait_weight(trait_file, rarity_weights):
    if ('#' in trait_file):
        print('# FOUND IN TRAIT FILE ', trait_file)
        trait_weight = int(trait_file.split('#')[1])
    else:
        trait_weight = 1
    rarity_weights.append(trait_weight)
    return rarity_weights


# Turns object into a string that gets added to generated_trait_list for ensuring trait selection is unique 
def generate_string_of_traits(trait_obj):
    trait_str = ''
    for key in trait_obj.keys():
        trait_str+=(key + trait_obj[key])
    return trait_str