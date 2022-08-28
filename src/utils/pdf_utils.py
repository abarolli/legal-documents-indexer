from ctypes import ArgumentError
from multiprocessing.sharedctypes import Value
from pathlib import Path
import pdf2image

from constants.images import ImageType


def convert_to_images(pdf_path:Path, outdir:Path=None, img_type:ImageType=ImageType.JPG):
    if pdf_path.suffix != ".pdf":
        return None

    if not outdir.exists():
        outdir.mkdir(parents=True)
    
    if img_type == ImageType.JPG:
        img_type, img_stem = "JPEG", ".jpg"
    elif img_type == ImageType.PNG:
        img_type, img_stem = "PNG", ".png"
    else:
        raise ArgumentError("ImageType should be ImageType.JPG or ImageType.PNG")

    images = pdf2image.convert_from_path(pdf_path)
    for i in range(len(images)):
        image = images[i]
        image.save(outdir / f"{pdf_path.stem}{i}{img_stem}", img_type)