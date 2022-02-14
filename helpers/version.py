import pathlib

from sqlalchemy import JSON


def get_project_version() -> JSON:
    return pathlib.Path('version.txt').read_text().strip()
