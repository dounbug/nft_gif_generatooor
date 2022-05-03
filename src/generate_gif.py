from PIL import Image
from config import *
from classes.Metadata import Metadata
from datetime import datetime
import time
import json

# Takes in an ordered list of paths from which to generate the final GIF
def generate_single_gif(iter, trait_paths):
    images = []
    base_path = trait_paths[0]

    for i in range (0,25):
        #Set background as the base for each incoming layer 
        base_image = Image.open(os.path.join(base_path, str(i)+'.png')).convert("RGBA")
        base = base_image.copy()
        for file_path in trait_paths[1:]:
            img = Image.open(os.path.join(file_path, str(i)+'.png')).convert("RGBA")
            base.paste(img, (0,0), img)
        images.append(base)

    save_gif(iter, images)
    

# Saves GIF to build/images directory 
def save_gif(iter, images):
    file_name = str(iter)+'.gif'

    images[0].save(os.path.join(SAVE_IMAGE_PATH, file_name), format='GIF', save_all=True, append_images=images[1:], optimize=True, loop=0)

    file_size = os.path.getsize(os.path.join(SAVE_IMAGE_PATH, file_name))
    print('GIF {} has been saved with a file size of {} MB'.format(iter, file_size))

# Generates metadata from defined class & passes JSON object to save function
def generate_metadata(iter, trait_obj):
    name = METADATA_NAME+' #'+str(iter)
    description = METADATA_DESCRIPTION
    edition = str(iter)
    date = time.mktime(datetime.now().timetuple())
    attributes = []
    for key in trait_obj:
        attributes.append({'trait_type': key, 'trait_value': trait_obj[key]})

    data = Metadata(name,description,edition,date,attributes)
    save_metadata(iter, data)
    

# Saves JSON metadata for the GIF to build/json directory
def save_metadata(iter, data):
    json_data = json.dumps(data.__dict__, indent=4)
    print('save metadata ', json_data)
    file_name = str(iter)+'.json'
    save_path = os.path.join(SAVE_METADATA_PATH, file_name)
    print('SAVE JSON FILE ', save_path)

    with open(save_path, "w") as outfile:
        outfile.write(json_data)


#TO DO: make sure base path comes in first at either fine_filepaths or gen_single_image level. is background always guaranteed?
#TO DO: file size check