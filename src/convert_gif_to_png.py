from PIL import Image
from config import *

# Loops over all directories in the defined gif_layers path to find .gif files to convert to separate .png files
# Only uses layers with subdirectory names matching those defined in config file LAYERS_ORDER
def get_layer_directories(path): 
    for subdir in os.listdir(path):
        if subdir in LAYERS_ORDER:
            print('Started writing PNG files for GIF trait type: ', subdir)
            parse_layer_directory(os.path.join(path, subdir), subdir)
            print('Completed writing PNG files for GIF trait type: ', subdir)


# Recursively parses through all subdirectories of a given layer's directory & sends .gif files to be deconstructed
def parse_layer_directory(subdir, folder_path):
    for file in os.listdir(subdir):
        d = os.path.join(subdir, file)
        if os.path.isdir(d):
            parse_layer_directory(d, os.path.basename(subdir)+'/'+file)
        elif file.endswith('.gif'):
            deconstruct_gif(subdir, folder_path, file)


# Takes a GIF & saves it as a sequence of PNG files in the defined GIF_DECONSTRUCTED_LAYERS_FOLDER
def deconstruct_gif(subdir, folder_path, file):
    gif_obj = Image.open(os.path.join(subdir, file))
    save_dir = os.path.join(GIF_DECONSTRUCTED_LAYERS_PATH, folder_path, os.path.splitext(file)[0]) 

    # Creates a subdirectory for each trait value within a trait type folder
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if(gif_obj.n_frames != 120):
        print('NOT 120 FRAMES FOUND:', subdir, file, gif_obj.n_frames)

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
get_layer_directories(GIF_LAYERS_PATH)

#TO DO: make sure files and sub-folders dont have the same name 