# NFT_GIF_GENERATOOOR
Generate a collection of NFTs as GIFs👾

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
- Subdirectory names must match layer names in [LAYERS_ORDER](https://github.com/0xDounia/nft_gif_generatooor/blob/main/src/config.py#L10) in order to be processed
- Nested folders within those subdirectories will be parsed for their GIF files as well (Ex: hair_2). This is done so that GIF layers that need to be built in a different order than LAYERS_ORDER are supported as well. See [Options](#Options) for more


# How To Run 🏃‍♀️
1. From the **nft_gif_generatooor** directory, run the below command for a 1 time conversion of all GIF files into their separate PNG files required to produce the final GIFs. These files will be stored in the [GIF_DECONSTRUCTED_LAYERS_PATH]([config.py](https://github.com/0xDounia/nft_gif_generatooor/blob/main/src/config.py)), which will be built upon the first run.
```
python3 src/convert_gif_to_png.py
```

# Options 🎛
- *SAVE_AS_MP4* - Toggle between saving the output file as a .gif or .mp4 using this boolean
