import os
from tempfile import mkdtemp

from django.core.files import File

from filer.models.filemodels import File as FilerFile
from filer.models.foldermodels import Folder as FilerFolder
from filer.models.imagemodels import Image as FilerImage
from filer.utils.compatibility import PILImage, PILImageDraw


# from https://github.com/divio/django-filer/blob/develop/tests/helpers.py#L46-L52
def create_image(mode="RGB", size=(800, 600)):
    """
    Creates a usable image file using PIL
    :returns: PIL Image instance
    """
    image = PILImage.new(mode, size)
    draw = PILImageDraw.Draw(image)
    x_bit, y_bit = size[0] // 10, size[1] // 10
    draw.rectangle((x_bit, y_bit * 2, x_bit * 7, y_bit * 3), "red")
    draw.rectangle((x_bit * 2, y_bit, x_bit * 3, y_bit * 8), "red")

    return image


def get_image(image_name="test_file.jpg"):
    """
    Creates and stores an image to the file system using PILImage

    :param image_name: the name for the file (default "test_file.jpg")
    :returns: dict {name, image, path}
    """
    image = create_image()
    image_path = os.path.join(
        mkdtemp(),
        image_name,
    )
    image.save(image_path, "JPEG")

    return {
        "name": image_name,
        "image": image,
        "path": image_path,
    }


def get_file(file_name="test_file.pdf"):
    """
    Creates and stores an arbitrary file into a temporary dir

    :param file_name: the name for the file (default "test_file.pdf")
    :returns: dict {name, image, path}
    """
    file_path = os.path.join(
        mkdtemp(),
        file_name,
    )
    data = open(file_path, "a")

    return {
        "name": file_name,
        "file": data,
        "path": file_path,
    }


def get_filer_image(image_name="test_file.jpg", name="",
                    original_filename=True):
    """
    Creates and stores an image to filer and returns it

    :param image_name: the name for the file (default "test_file.jpg")
    :returns: filer image instance
    """
    image = get_image(image_name)
    filename = None
    if original_filename:
        filename = image.get("name")
    filer_file = File(
        open(image.get("path"), "rb"),
        name=image.get("name"),
    )
    filer_object = FilerImage.objects.create(
        original_filename=filename,
        file=filer_file,
        name=name,
    )

    return filer_object


def get_filer_file(file_name="test_file.pdf", folder=None):
    """
    Creates and stores a file to filer and returns it

    :param file_name: the name for the file (default "test_file.pdf")
    :param folder: optionally provide a folder instance
    :returns: filer file instance
    """
    data = get_file(file_name)
    filer_file = File(
        open(data.get("path"), "rb"),
        name=data.get("name"),
    )
    filer_object = FilerFile.objects.create(
        original_filename=data.get("name"),
        file=filer_file,
        folder=folder,
    )

    return filer_object


def get_filer_folder(folder_name="test_folder", parent=None):
    """
    Creates and returns a filer folder

    :param folder_name: the name of the folder to be used (default "test_folder")
    :param parent: optionally provide a parent folder
    :returns: filer folder instance
    """
    filer_object = FilerFolder.objects.create(
        parent=parent,
        name=folder_name,
    )

    return filer_object
