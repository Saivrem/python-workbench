from disk_utils.file_consumer import FileConsumer


class FileLister(FileConsumer):
    __slots__ = ["files_list"]

    def __init__(self):
        self.files_list = []

    def accept(self, file) -> None:
        self.files_list.append(file)
