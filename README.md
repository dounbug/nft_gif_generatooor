# NFT_GIF_GENERATOOOR
Generate a collection of NFTs as GIFs👾

## Local Setup 💻
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

## File Structure 🌳
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
| -- face
| ----- face_1.gif
| ----- face_2.gif

```
 - Subdiretory names must match layer names in **LAYERS_ORDER** in order to be processed



## How To Run 🏃‍♀️
1. From the **nft_gif_generatooor** directory, run the below command for a 1 time conversion of all GIF files into their separate PNG files required to produce the final GIFs. These files will be stored in the _GIF_DECONSTRUCTED_LAYERS_PATH_ defined in [config.py] (https://github.com/0xDounia/nft_gif_generatooor/blob/main/src/config.py), which will be built upon the first run.
```
python3 src/convert_gif_to_png.py
```

