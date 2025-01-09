from os import path, listdir

from disk_utils.file_consumer import FileConsumer


class FileWalker:
    __slots__ = ["root", "consumer"]

    def __init__(self, root: str, consumer: FileConsumer):
        self.root = root
        self.consumer = consumer

    def list_files(self, root_dir: str = None):
        current = root_dir or self.root
        if path.exists(current):
            try:
                dir_list = [current]

                while dir_list:
                    current = dir_list.pop()
                    for item in listdir(current):
                        full_path = path.join(current, item)
                        if path.isdir(full_path):
                            dir_list.append(full_path)
                            continue
                        self.consumer.accept(full_path)
            except OSError as e:
                print(f"Error while processing {current}: {e}")
