import shutil

from disk_utils.consumer.file_consumer import FileConsumer
from pathlib import Path


class FileMover(FileConsumer):
    __slots__ = ['path_map']

    def __init__(self, path_map: dict[str, str]):
        """
        Initializes FileMover with a mapping of file extensions to target directories.

        :param path_map: Dictionary mapping file extensions (without dot) to target directories.
        :type path_map: dict[str, str]
        """
        super().__init__()
        self.path_map = path_map

    def is_applicable(self, path) -> bool:
        extension = path.suffix.lower()[1:]
        return extension in self.path_map and path.exists() and path.is_file()

    def accept(self, path) -> None:
        extension = path.suffix.lower()[1:]

        target_dir = self.prepare_path(extension)
        shutil.move(str(path), str(target_dir / path.name))
        print(f"file {path.name} moved to {target_dir}")

    def prepare_path(self, key) -> Path:
        path = Path(self.path_map[key])
        path.mkdir(parents=True, exist_ok=True)
        return path
