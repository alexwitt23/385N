import pathlib

_IMG_EXTS = [".jpeg", ".jpg", ".png"]


def find_all_images(image_folder: pathlib.Path):
    images = []
    for ext in _IMG_EXTS:
        images += list(image_folder.rglob(f"*{ext}"))
        images += list(image_folder.rglob(f"*{ext.upper()}"))
    return images