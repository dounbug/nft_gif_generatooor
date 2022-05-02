from PIL import Image
from config import *

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

    save_gif(images, iter)
    

# Saves GIF to build directory 
def save_gif(images, iter):
    file_name = str(iter)+'.gif'

    images[0].save(os.path.join(SAVE_IMAGE_PATH, file_name), format='GIF', save_all=True, append_images=images[1:], optimize=True, loop=0)

    file_size = os.path.getsize(os.path.join(SAVE_IMAGE_PATH, file_name))
    print('GIF {} has been saved with a file size of {} MB'.format(iter, file_size))

#TO DO: make sure base path comes in first at either fine_filepaths or gen_single_image level. is background always guaranteed?
#TO DO: file size check