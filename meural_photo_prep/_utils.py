from multiprocessing import Pool
import os
import threading
from PIL import Image
import queue


def _create_folder_structure(output_folder):
    """
    Create the folder structure for the output files
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    subfolder = os.path.join(output_folder, "meural1")
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)


def _get_image_file_paths_from_folder(input_folder: os.path) -> list:
    """
    Get the image paths from a folder
    """
    images = []
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith((".jpg", ".jpeg", ".png", ".bmp", ".svg")): 
                images.append(file_path)
    return images


def _process_images(image_path: str, output_folder: str):
    """
    Process the images for the Meural
    """
    image = Image.open(image_path)
    filename, extension = (image.filename.split("/")[-1]).split(".")
    filename = "".join(ch for ch in filename if ch.isalnum())
    image.filename = filename + "." + extension
    image.save(os.path.join(output_folder, "meural1", image.filename))
    # save the image to the output folder

    # create a thumbnail
    thumb = image.copy()
    thumb.thumbnail((120, 68))
    thumb.filename = filename + "-thumb." + extension
    thumb_path = os.path.join(output_folder, "meural1", thumb.filename)
    thumb.save(os.path.join(output_folder, "meural1", thumb.filename))
    os.rename(
        thumb_path,
        thumb_path.replace(
            "-thumb." + extension,
            "." + extension + ".thumb"
        )
    )
    thumb.close()
    image.close()


# Function to take the queue of images and process them threaded
def _process_image_queue(images: list, output_folder: str):
    """
    Process the images in the queue
    """
    pool = Pool(processes=os.cpu_count())
    args = [(i, output_folder) for i in images]
    _ = pool.starmap(_process_images, args)

        

# Wrapper function to process the images
def prep_photos(input_folder: str, output_folder: str):
    """
    Wrapper function to process the images
    """
    _create_folder_structure(output_folder)
    images = _get_image_file_paths_from_folder(input_folder)
    _process_image_queue(images, output_folder)
