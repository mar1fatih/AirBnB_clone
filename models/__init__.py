#!/usr/bin/python3
"""init file to access storage"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
