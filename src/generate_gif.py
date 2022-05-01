from config import *

# Converts mapping of selected trait type: trait value pairs into a list of paths in which to find the deconstructed GIFs
def find_filepaths(image_traits):
    filepaths = []
    for k in image_traits.keys():
        file_path = os.path.join(GIF_DECONSTRUCTED_LAYERS_PATH, k, image_traits[k]) 
        filepaths.append(file_path)
    return filepaths


# Takes in an ordered list of paths from which to generate the final GIF
def generate_single_image(filepaths):
    print('Generating image 0')
    images = []
    base_path = filepaths[0]

    for i in range (0,120):
        #Set background as the base for each incoming layer 
        base_image = Image.open(os.path.join(base_path, str(i)+'.png')).convert("RGBA")
        base = base_image.copy()

        for file_path in filepaths[1:]:
            img = Image.open(os.path.join(file_path, str(i)+'.png')).convert("RGBA")
            base.paste(img, (0,0), img)
        images.append(base)

    save_gif(images)
    

def save_gif(images):
    if not os.path.exists(BUILD_PATH):
        os.makedirs(BUILD_PATH)

    images[0].save(str(BUILD_PATH) + '/TESTING.gif', format='GIF', save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)

#TO DO: make sure base path comes in first at either fine_filepaths or gen_single_image level. is background always guaranteed?