from PIL import Image
from config import *
from classes.Metadata import Metadata
from datetime import datetime
import time
import json

# Takes in an ordered list of paths from which to generate the final GIF
def generate_single_gif(iter, trait_paths):
    base_path = trait_paths[0]

    for i in range (0,NUMBER_OF_FRAMES-1): 
        #Set background as the base for each incoming layer 
        base_image = Image.open(os.path.join(base_path, str(i)+'.png')).convert("RGBA")
        base = base_image.copy()
        for file_path in trait_paths[1:]:
            img = Image.open(os.path.join(file_path, str(i)+'.png')).convert("RGBA")
            base.paste(img, (0,0), img)

        # Save the individual PNG
        image_path = os.path.join(SAVE_IMAGE_PATH, str(i)+'.png')
        base.save(image_path, format='PNG')

        # If save thumbnail is on, save the first image now
        if(i == 0 and SAVE_THUMBNAIL):
            base.save(os.path.join(SAVE_THUMBNAIL_PATH, str(iter)+'.png'), format='PNG')

    save_mov(iter)


# Saves GIF to build/images directory 
def save_mov(iter):
    gif_path = os.path.join(SAVE_IMAGE_PATH, str(iter)+'.mp4')

    # Change directory to run the generation code, save movie, thumbnail delete PNGs, & revert directory back 
    os.chdir(SAVE_IMAGE_PATH)
    os.system("ffmpeg -framerate {} -i %d.png -c:v libx264 {}.mp4".format(FRAME_RATE, iter))
    os.system(' find . -name "*.png" -type f -delete ')
    os.chdir(BASE_PATH)

    # Get file size 
    file_size = os.path.getsize(gif_path)
    print('GIF {} has been saved with a file size of {} MB'.format(iter, file_size))


# Generates metadata from defined class & passes JSON object to save function
def generate_metadata(iter, trait_obj):
    name = METADATA_NAME.join(' #').join(str(iter))
    desc = METADATA_DESCRIPTION
    edition = str(iter)
    date = time.mktime(datetime.now().timetuple())
    thumbnail = ''
    attributes = []
    for key in trait_obj:
        attributes.append({'trait_type': key, 'trait_value': trait_obj[key]})

    data = Metadata(name,desc,edition,date,thumbnail,attributes)
    save_metadata(iter, data)
    

# Saves JSON metadata for the GIF to build/json directory
def save_metadata(iter, data):
    json_data = json.dumps(data.__dict__, indent=4)
    file_name = str(iter)+'.json'
    save_path = os.path.join(SAVE_METADATA_PATH, file_name)

    with open(save_path, "w") as outfile:
        outfile.write(json_data)


#TO DO: make sure base path comes in first at either fine_filepaths or gen_single_image level. is background always guaranteed?
#TO DO: file size check