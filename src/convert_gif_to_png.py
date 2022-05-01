from PIL import Image
from config import *

# Loops over all directories in the defined gif_layers path to find .gif files to convert to separate .png files
# Only uses layers with subdirectory names matching those defined in config file LAYERS_ORDER
def find_gif_files(): 
    for subdir, dir, file in os.walk(GIF_LAYERS_PATH):
        subdir_name = os.path.split(subdir)[1]
        if subdir_name in LAYERS_ORDER:
            # Only parse gif paths that match directory name with layers in LAYERS_ORDER
            for file in os.listdir(subdir):
                if file.endswith('.gif'):
                    deconstruct_gif(subdir, file)
            print('Completed writing PNG files for GIF trait type: ', subdir_name)


# Takes a GIF & saves it as a sequence of PNG files in the defined GIF_DECONSTRUCTED_LAYERS_FOLDER
def deconstruct_gif(subdir, file):
    gif_obj = Image.open(os.path.join(subdir, file))
    save_dir = os.path.join(GIF_DECONSTRUCTED_LAYERS_PATH, os.path.basename(os.path.normpath(subdir)), os.path.splitext(file)[0]) 

    # Creates a subdirectory for each trait value within a trait type folder
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Loop over every frame in the GIF, creating the directories as needed & saving each file as png 
    try:
        frame = 0
        while frame in range(0, gif_obj.n_frames):
            save_path = str(os.path.join(save_dir, str(frame)))+'.png'
            # In the case that new files need to be added without rewriting over all existing deconstructed layers, only save if path not present
            if not os.path.isfile(save_path):
                gif_obj.seek(frame)
                gif_obj.save(save_path, 'PNG')
            frame+=1
    except EOFError as e:
        print(e, subdir+'/'+file)


# Run main function
find_gif_files()
