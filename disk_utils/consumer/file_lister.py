from disk_utils.consumer.file_consumer import FileConsumer


class FileLister(FileConsumer):
    __slots__ = ["files_list"]

    def __init__(self):
        self.files_list = []

    def accept(self, path) -> None:
        self.files_list.append(path)

    def print(self):
        if self.files_list:
            for file in self.files_list:
                print(f'{file}')