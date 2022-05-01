# NFT_GIF_GENERATOOOR
Generate a collection of NFTs as GIFs👾

### Local Setup
###### To develop and test locally, a virtual environment will need to be created
```
$ pip3 install virtualenv
$ cd nft_gif_generatooor/
$ virtualenv env
$ source env/bin/activate
$ pip3 install requests
```
###### To see what packages are in your virtual environment
```
pip list
```
###### To deactivate
```
deactivate
```

### File Setup
###### gif_layers
-All trait types should have their GIFs in a respective folder within gif_layers
-Nested folder structure is not supported



### How To Run
1. From the nft_gif_generatooor directory run the below command for a 1 time conversion of all GIF files into their separate PNG files required to produce final GIF. These files will be stored in the GIF_DECONSTRUCTED_LAYERS_PATH defined in config.py. If left unchanged, this should create a '/gif_deconstructed_layers' subdirectory within your local copy of the repo.
```
python3 src/convert_gif_to_png.py
```

