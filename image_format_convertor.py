from pathlib import Path
from PIL import Image


def convert_image_format(main_path='.', mode="RGB", result_exten=".png"):
    """main_path can be a dir in which contains your images
        or an image path
     """
    # About image mode
    # https://pillow.readthedocs.io/en/stable/handbook/concepts.html?highlight=mode#modes
    image_modes = ['1', 'L', 'P', 'RGB', 'RGBA',
                   'CMYK', 'YCBCr', 'LAB', 'HSV',
                   'I', 'F']

    # About image format
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#image-file-formats
    image_suffix = ['.jpg', '.jpeg', '.tiff', '.png',
                    '.bmp', '.heif', '.bat']

    if mode not in image_modes:
        raise ValueError(f"bad mode {repr(mode)}")

    main_path = Path(main_path)
    if not main_path.exists():
        print("File doesn't exist")
        return

    is_dir = main_path.is_dir()
    result_dir_name = 'result_images'

    if is_dir:
        result_path = main_path / result_dir_name
    else:
        result_path = main_path.parent / result_dir_name

    if not result_path.exists():
        try:
            result_path.mkdir(mode=0o751, parents=True, exist_ok=True)
        except (FileExistsError, FileNotFoundError) as err:
            print("directory is exist")

    if is_dir:
        sub_filepaths = [p for p in main_path.glob('*.*') if p.suffix in image_suffix]
        for p in sub_filepaths:
            image = Image.open(p)
            image = image.convert(mode)
            f, e = p.name.split('.')
            file_name = f + result_exten
            image_path = result_path / file_name
            image.save(fp=image_path)
    elif main_path.is_file():
        result_path = result_path / main_path.name
        result_path = result_path.with_suffix(result_exten)
        image = Image.open(main_path)
        image = image.convert(mode)
        image.save(fp=result_path)

if __name__ == "__main__":
    pass
    # eg
    # convert_image_format(main_path = "./images", mode="P", result_exten=".png")