from .library import Library

def load_library(filepath):
    library = Library()
    library.load_from_file(filepath)
    return library

def save_library(library, filepath):
    library.save_to_file(filepath)
