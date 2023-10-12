#!/usr/bin/python3
"""This model links filestorage to basemodel"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
