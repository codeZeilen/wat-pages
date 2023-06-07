import pathlib
import sys

from wat.pagesources.GlobTrie import GlobTrie

def path_of_page(page_file_name):
    with open(page_file_name, 'r') as f:
        content = f.read()
    header = content.split("---")[1].strip()
    
    header_dict = dict()
    for line in header.splitlines():
        separator = line.find(":")
        key = line[:separator].strip()
        value = line[separator+1:].strip()
        header_dict[key] = value
    if 'path' not in header_dict:
        print(f"Page {page_file_name} does not have a path. Header values are: {header_dict}")
        sys.exit(1)
    path = header_dict['path']
    if not path[0] == '/':
        # Ensure that relative paths are included as such
        path = './' + path
    return path

def is_page(file: pathlib.Path):
    return file.is_file() and file.name.endswith('.md')

def is_path_valid(path):
    if path.startswith('/'):
        # Only single globs can be used in absolute paths
        return path.count('**') == 0
    else:
        # Relative paths should not contain directories
        return path.count('/') <= 1
        
def build_index_for(folder):
    result = GlobTrie()
    for file_path in pathlib.Path('./fs-path-pages').iterdir():
        if is_page(file_path):
            path = path_of_page(file_path)
            if not is_path_valid(path):
                print(f"Invalid path: {path} for page {file_path}")
                sys.exit(1)
            result.add(path, file_path.name)
    return result.store_string()


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Usage: python3 {sys.argv[0]} <folder>")
        sys.exit(1)

    folder = pathlib.Path(sys.argv[1])
    print(build_index_for(folder))
