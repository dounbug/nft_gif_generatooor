from generate_gif import *
from randomly_generate_traits import *

# Starts creating the random GIFs
def start_creating():
    for i in range(GENERATION_COUNT):
        traits = generate_trait_paths()

        # Generate & save the image
        print('Generating GIF {} with traits: {} '.format(i, traits[0]))
        generate_single_gif(i, traits[1])

        # Generate & save the metadata





start_creating()