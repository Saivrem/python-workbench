from pathlib import Path
import logging

from disk_utils.consumer.file_consumer import FileConsumer


class FileWalker:
    __slots__ = ["root", "consumers"]

    def __init__(self, root: str, consumers: list[FileConsumer,]):
        self.root = Path(root)
        if not consumers:
            raise ValueError("consumer_list cannot be empty.")
        self.consumers = consumers

    def walk_file_tree(self, root_dir: Path = None):
        """Walks file tree and then passes processing to corresponding methods"""
        current = Path(root_dir) if root_dir else self.root
        if not current.exists():
            logging.warning(f"Path does not exist: {current}")
            return

        try:
            self._process_directory(current)
        except OSError as e:
            logging.error(f"Error while processing {current}: {e}")

    def _process_directory(self, directory: Path):
        """Recursively process directory and route to file processing"""
        stack = [directory]

        while stack:
            current = stack.pop()
            try:
                for item in current.iterdir():
                    if item.is_dir():
                        stack.append(item)
                        continue

                    self._process_file(item)
            except OSError as e:
                logging.error(f"Failed to access {current}: {e}")

    def _process_file(self, file_path: Path):
        """Passes file to corresponding consumers"""
        for consumer in self.consumers:
            try:
                if consumer.is_applicable(file_path):
                    consumer.accept(file_path)
            except Exception as e:
                logging.error(f"Error processing {file_path} with {consumer}: {e}")
