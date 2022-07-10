# NFT_GIF_GENERATOOOR
Generate a collection of NFTs as GIFs👾 (In Progres..)

# Local Setup 💻
#### To develop and test locally, a virtual environment will need to be created
```
$ pip3 install virtualenv
$ cd nft_gif_generatooor/
$ virtualenv env
$ source env/bin/activate
```
#### To install required packages
```
$ pip3 install requests
```
#### To see what packages are in your virtual environment
```
$ pip list
```
#### To deactivate
```
$ deactivate
```

# File Structure 🌳
### gif_layers
```js
gif_layers
| -- background
| ----- background_1.gif
| ----- background_2.gif
| ----- background_3.gif
| -- body
| ----- body_1.gif
| ----- body_2.gif
| ----- body_3.gif
| ----- body_4.gif
| -- hair
| ----- hair_1.gif
| ----- hair_2
| -------- hair_2_front.gif
| -------- hair_2_back.gif
| ----- hair_3.gif
| -- face
| ----- face_1.gif
| ----- face_2.gif

```
- No spaces!
- Subdirectory names must match layer names in [LAYERS_ORDER](https://github.com/0xDounia/nft_gif_generatooor/blob/main/src/config.py#L10) in order to be processed
- Nested folders within those subdirectories will be parsed for their GIF files as well (Ex: hair_2). This is done so that GIF layers that need to be built in a different order than LAYERS_ORDER are supported as well. See [Config Constants & Options](#Options) for more

# How To Run 🏃‍♀️
1. Create a folder called 'gif_layers' and input all trait folders with their named attributes [follow syntax above].
2. From the **nft_gif_generatooor** directory, run the below command for a 1 time conversion of all GIF files into their separate PNG files required to produce the final GIFs. These files will be stored in the [GIF_DECONSTRUCTED_LAYERS_PATH]([config.py](https://github.com/0xDounia/nft_gif_generatooor/blob/main/src/config.py)), which will be built upon the first run.
```
python3 src/convert_gif_to_png.py
```
3. From the same directory, once the frames of all GIFs have been parsed into PNG's & saved into their subdirectories, run the below command to build.
```
python3 src/main.py
```

# Config Constants & Options 🎛
- *NUMBER_OF_FRAMES* - This is a REQUIRED constant. Each GIF should be using the same # of frames to generate in order to properly overlap the GIFs into the final NFT. An error will be thrown from the convert_gif_to_png.py script 
- *GENERATION_COUNT* - The total number of NFTs that will be randomly generated
- *SAVE_AS_MP4* - Toggle between saving the output file as a .gif or .mp4 using this boolean
- *METADATA_NAME* - Name of the collection that will be placed in the 'name' key in the metadata JSON object 
- *PARSE_UNDERSCORE* - Boolean to turn ON if underscores should be replaced with spaces in attribute value names when being saved in the 
- *GIF_DURATION* - Duration in seconds of the final output.

# Metadata Format 📀
* name: METADATA_NAME,
* description: METADATA_DESCRIPTION,
* edition: Numeric value of NFT edition (0, 1, 2, 3, etc.),
* date: Date in UNIX,
* thumbnail": "",
* attributes : List of {attribute type: attribute value} objects.
