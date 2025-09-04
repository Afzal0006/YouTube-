import os

def file_size(path):
    size = os.path.getsize(path)
    return round(size / (1024*1024), 2)  # in MB
