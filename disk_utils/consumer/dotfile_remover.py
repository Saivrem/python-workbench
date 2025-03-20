from disk_utils.consumer.file_consumer import FileConsumer


class DotFileRemover(FileConsumer):
    __slots__ = ["dry_run"]

    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run

    def is_applicable(self, path) -> bool:
        return path.exists() and path.is_file() and path.name.startswith(".")

    def accept(self, path) -> None:
        if not self.dry_run:
            path.unlink()
            print(f'dotfile {path} removed')
        elif self.dry_run:
            print(f'dotfile {path} found')
