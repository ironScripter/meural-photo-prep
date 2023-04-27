# Netgear Meural Photo Preparation
Python Package to prepare photos for use with Netgear Meural Picture Frames. \
__This package is not affiliated with Netgear in any way.__ \
Netgear Meural Picture Frames require photos to be formatted in a specific way. \
This package will prepare photos for use with Netgear Meural Picture Frames. \
For more information on the Netgear Meural Picture Frames formatting need please visit
[Netgear](https://kb.netgear.com/000064426/How-do-I-add-images-or-videos-to-a-memory-card-for-my-Meural)
## Table of Contents
* [External Dependencies](#external-dependencies)
* [Installation](#installation)
* [Usage](#usage)

## External Dependencies
* [Pillow](https://pillow.readthedocs.io/en/stable/)
## Installation
### Requirements
* Python 3.10+

### PIP
```bash
pip install meural-photo-prep
```
### Poetry
```yaml
[tool.poetry]
name = "example-package"
version = "0.1.0"
description = ""
authors = ["Example developer <dev@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"
meural-photo-prep = "^1.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## Usage
### Description
* Prepares photos for use with Netgear Meural Picture Frames.
* Copies photos from the input path to the output path. 
  * Removes special characters from the file name.
* Creates a thumbnail for each photo using the 
[Thumbnail()](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail) 
method from Pillow.
  * The thumbnail is created using the dimensions specified in the documentation above.
  * The thumbnail is saved with the same name as the original photo with the addition of the .thumb extension.
* Function uses threading to process photos in parallel. 
  * **__NOTE: This may cause issues with memory usage as thread limits are not implemented in this version \
  be careful how many photos you give it!__**
### Example
```python
import meural_photo_prep as mpp

mpp.prep_photos("<INPUT_PATH>", "<OUTPUT_PATH>")
```
#### Output
```bash
<OUTPUT_PATH>
|__ meural1
    |__ img1.jpg # All names have special characters removed
    |__ img1.jpg.thumb # Rendered by Pillow using Thumbnail() method
    |__ img2.jpg
    |__ img2.jpg.thumb
    |__ img3.jpg
    |__ img3.jpg.thumb
