# AuOC
Augmentation On Coordinates provides a away to make image changing functions based on coordinates

# Files to choose from:

`main.py` enables the manual handling of the images. It will load the images, and the given functions specified in `funcsToCall.py` 

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
