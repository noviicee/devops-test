import pathlib


def get_project_version() -> str:
    return pathlib.Path('version.txt').read_text().strip()
