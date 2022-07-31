from generate_gif import *
from randomly_generate_traits import *
import shutil

# Main function call 
def main():
    create_directories()
    start_creating()


# Starts creating the random GIFs
def start_creating(): 
    for i in range(GENERATION_COUNT):
        traits = generate_traits()

        # Generate & save the image
        print('\nGenerating GIF {} with traits: {} '.format(i, traits[0]))
        generate_single_gif(i, traits[1])

        # Generate & save the metadata
        generate_metadata(i, traits[0])


# Deletes & re-creates build directory at the beginning of every generation
def create_directories():
    if os.path.exists(BUILD_PATH):
        shutil.rmtree(BUILD_PATH)
    os.mkdir(BUILD_PATH)
    os.mkdir(SAVE_IMAGE_PATH)
    os.mkdir(SAVE_METADATA_PATH)
    os.mkdir(SAVE_THUMBNAIL_PATH)


main()