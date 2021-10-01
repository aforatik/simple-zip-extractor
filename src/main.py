# ========== Imports ===========
import zipfile
from tabulate import tabulate

# =============== Useful variables ============

query_input = None

available_operations = '''========  Operations  ======== :
    1) Extract all
    2) Selective extract
    3) Search files with extension name
    4) List all file information within this archive
    5) Count all file types
    6) Count Specific file types
    7) Extract specific file types
    8) Exit
    \n'''


# =========== Useful functions =============

def title_center_align(title: str, width: int, fill_char: str = ' ', gap_between: int = 0):
    print(title.center(len(title) + gap_between * 2, " ").center(len(title) + (gap_between + width) * 2, fill_char))


def show_children_files_info():
    children_file_info = {"file": [], "size": [], 'is Folder': [], 'compress type': [], 'compress size': []}
    for file in archive_file.filelist:
        name = file.filename
        size = file.file_size
        children_file_info['file'].append(name)
        children_file_info['size'].append(str(size) + " byte")
        children_file_info['is Folder'].append(file.is_dir())
        children_file_info['compress type'].append(file.compress_type)
        children_file_info['compress size'].append(file.compress_size)
    print(tabulate(children_file_info, headers='keys', tablefmt='fancy_outline',
                   showindex=range(1, len(archive_file.filelist) + 1)))


def show_base_file_info():
    directory_count = 0
    for file in archive_file.filelist:
        if file.is_dir():
            directory_count += 1
        else:
            print("{} creation date : last modified on {}/{}/{} at {}:{}:{}".format(
                file.filename.rpartition('/')[-1], *file.date_time))
    print("filename : ", archive_file.filename)
    print("number of children files : ", len(archive_file.filelist))
    print("children folders : ", directory_count)


def get_files_with_extension(extension: str):
    search_result = []
    for file in archive_file.filelist:
        actual_file_name = str(file.filename.rpartition('/')[-1])
        if actual_file_name.rpartition('.')[-1].lower() == extension.rpartition('.')[-1].lower():
            search_result.append(actual_file_name)
    return search_result


def show_results(search_query):
    extension_name: str = search_query
    print("searching result with input ... {}".format(search_query))

    search_results = get_files_with_extension(extension=extension_name)
    count_search_result = len(search_results)
    search_result_table = {"{} results found".format(count_search_result): search_results}
    print(tabulate(search_result_table, headers='keys', tablefmt='fancy_outline'))


def extract_all_files():
    print("test function")
    pass


def no_use():
    print("Functionality not added...")


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

        # 1) Extract all
        # 2) Selective extract
        # 3) Search files with extension name
        # 4) List all file information within this archive
        # 5) Count all file types
        # 6) Count Specific file types
        # 7) Extract specific file types
        # 8) Exit

        while True:
            print(available_operations)
            operation = input(">> ").strip()

            # ======= Extract all files =======
            if operation == '1':
                no_use()
                input("....continue....".center(50))
            # ======= Selective extract ========
            elif operation == '2':
                no_use()
                input("....continue....".center(50))
            elif operation == '3':
                query = input("enter extension name : ")
                show_results(search_query=query)
                input("....continue....".center(50))
            elif operation == '4':
                no_use()
                input("....continue....".center(50))
            elif operation == '5':
                no_use()
                input("....continue....".center(50))
            elif operation == '6':
                no_use()
                input("....continue....".center(50))
            elif operation == '7':
                no_use()
                input("....continue....".center(50))
            elif operation == '8':
                exit(0)
            else:
                print("please enter number between 1-8\n")
                input("....continue....".center(50))
