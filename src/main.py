# ========== Imports ===========
import zipfile
from tabulate import tabulate, izip_longest, _table_formats, _latex_row, tabulate_formats


# =========== Useful functions =============

def title_center_align(title: str, width: int, fill_char: str = ' ', gap_between: int = 0):
    print(title.center(len(title) + gap_between * 2, " ").center(len(title) + (gap_between + width) * 2, fill_char))


# =========== Enter file path ========

file_path = 'Day.zip'  # input("enter file path : ")
file_path = file_path.strip(" ")
if file_path == "":
    print("File path can't be empty!!")
else:
    try:
        archive_file = zipfile.ZipFile(file_path)
    except Exception as e:
        print(f"Error! {e.args[1]}")
    else:
        title_center_align(archive_file.filename, 10, "=", gap_between=2)

        def show_all_files_info():
            file_info = {"file": [], "size": [], 'Is Folder': []}
            for file in archive_file.filelist:
                name = file.filename
                size = file.file_size
                file_info['file'].append(name)
                file_info['size'].append(str(size) + " byte")
                file_info['Is Folder'].append(file.is_dir())
            print(tabulate(file_info, headers='keys', tablefmt='fancy_outline',
                           showindex=range(1, len(archive_file.filelist) + 1)))


        want_see_files = input("want to see all files in this archive ? yes(y) or no(n): ").lower()[0]
        if want_see_files == 'y':
            show_all_files_info()
