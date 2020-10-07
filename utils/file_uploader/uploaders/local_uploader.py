import os

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile


class LocalUploader:
    def __init__(self):
        self.__base_dir = settings.UPLOAD_DIR

    def upload(self, source_path, destination_path):
        pass

    def upload_in_memory_uploaded_file(self, image: InMemoryUploadedFile, directory: str, filename: str) -> None:
        self.__create_directory(directory)
        with open(f"{self.__base_dir}/{directory}/{filename}", "wb+") as file:
            for chunk in image.chunks():
                file.write(chunk)

    def delete(self, filename: str) -> None:
        if os.path.isfile(f"{self.__base_dir}/{filename}"):
            os.remove(f"{self.__base_dir}/{filename}")

    def __create_directory(self, folder_name: str) -> None:
        try:
            os.makedirs(f"{self.__base_dir}/{folder_name}/")
        except OSError:
            pass
