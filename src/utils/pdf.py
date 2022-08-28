from ctypes import ArgumentError
from multiprocessing.sharedctypes import Value
from pathlib import Path
from typing import Callable, List
import pdf2image

import numpy as np
from constants.images import ImageType


def convert_to_images(pdf_path:Path, outdir:Path, img_type:ImageType=ImageType.JPG, preprocessor:Callable=None) -> List[Path] | None:
    '''
    Converts the pdf at 'pdf_path' to an image of type jpeg or png (determined by 'img_type' param). The pdf \n
    pages are each saved as their own image in the 'outdir' folder. Each image is saved as the pdf name with\n
    an increment '-{i}' appended.\n

    Provide an optional 'preprocessor' function with will be passed the Images immediately after being converted\n
    from their pdf format. This 'preprocessor' will be called before the images are saved.
    '''
    if pdf_path.suffix != ".pdf":
        return None

    if not outdir.exists():
        outdir.mkdir(parents=True)
    
    if img_type == ImageType.JPG:
        img_type, img_stem = "JPEG", ".jpg"
    elif img_type == ImageType.PNG:
        img_type, img_stem = "PNG", ".png"
    else:
        raise ArgumentError("'img_type' should be ImageType.JPG or ImageType.PNG")

    images = pdf2image.convert_from_path(pdf_path)
    img_paths = []
    for i in range(len(images)):
        image = images[i]
        image = preprocessor(image)
        img_path = outdir / f"{pdf_path.stem}-{i}{img_stem}"
        img_paths.append(img_path)
        image.save(img_path, img_type)

    return img_paths