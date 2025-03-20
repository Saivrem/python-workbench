from pathlib import Path

class FileConsumer:

    def is_applicable(self, path: Path) -> bool:
        """should define if consumer is applicable"""
        return True

    def accept(self, path: Path) -> None:
        """ Functional interface emulation """
        raise NotImplementedError("Method is not implemented")