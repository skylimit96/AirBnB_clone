#!/usr/bin/python3
"""__init__ special Py file to indicate that it's a package """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
