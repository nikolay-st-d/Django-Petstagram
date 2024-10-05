from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, file_size_mb: float, message=None):
        self.file_size_mb = file_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f'File must be equal or below {self.file_size_mb}Mb'
        else:
            self.__message = value

    def __call__(self, file):
        if file.size > self.file_size_mb * 1024 * 1024:
            raise ValueError(self.message)
