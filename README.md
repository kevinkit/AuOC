# AuOC
Augmentation On Coordinates provides a away to make image changing functions based on coordinates and also manual by hand for fine adjusting. Call the scripts with the paramter "--h" to see further options.

# By Hand

`main.py` enables the manual handling of the images. It will load the images, and the given functions specified in `funcsToCall.py`. 

The augmentations done to the images are stored in save folder, or any other given parameter. 

# By automatic Script

Use the `AutoAugment.py`script, see the [json-File](https://github.com/kevinkit/AuOC/blob/master/saves/1582585262.2803874_unnamed.jpg.json)  for an example how to automize the process. All files stored by the `main.py` file are usable by the automatic script. 

The json file must have the following setup:

{"augmentations": [{"func_name": "makeRed", "coordinates": [39, 122, 84, 202]}, {"func_name": "makeRed", "coordinates": [97, 217, 255, 378]}], "filename": "images\\unnamed.jpg"}

Where the "augmentations" holds a list of augmentations. Each element in the list is another entry wher "func_name" is the name of the function that will be applied to the area given under the key "coordinates". Note that the function must be applied in `funcsToCall.py`. 
Lastly the key "filename" points to the file. You must use "\\" for the path. The filename will be used to store the results. 


## Adding custom functions

To add a custom function specify it in the `funcsToCall.py`. Then parse it as an argument to the `main.py` with the `--functions` flag, like this: 

  
```
python .\main.py --functions makeRed mosaic
```

This will enable the functions makeRed and mosaic. 

## HotKeys:

| Hotkey | Functionality          |
|--------|------------------------|
| d      | next image             |
| a      | previous image         |
| s      | save (changed) image   |
| m      | change mode to redo    |
| j      | previous functionality |
| k      | next functionality     |
