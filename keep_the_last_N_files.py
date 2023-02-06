from asyncio.windows_events import NULL
from msilib.schema import File
import os
import logging

class File(object):
    
    def __init__(self, root,  file_name) -> None:
        file_path = os.path.join(root, file_name)
        self.file_name = file_name
        self.file_modification_time = os.path.getmtime(file_path)
    
    def get_file_name(self):
        return self.file_name

    def get_file_modification_time(self):
        return self.file_modification_time

    def __lt__(self, other):
        return self.file_modification_time > other.file_modification_time

    

def main(root, n):
    logging.basicConfig(filename='remove.log', filemode = "w+", encoding='utf-8', level=logging.INFO)
    file_list = []
    for root, dirs, files in os.walk(root):
        for file in files:
            file_list.append(File(root, file))

    file_list.sort()

    file_list = file_list[n:]

    for file in file_list:
        logging.info('已刪除' + file.get_file_name())
        os.remove(os.path.join(root, file.get_file_name()))


if __name__ == "__main__":
    main(root = "", n = 0)
